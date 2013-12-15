# read_browser_databases

# Processes on-disk SQLite database files for Mozilla Firefox
# to search for private browsing artifacts

# Notes: Run using Python 3.3.3; some encrypted Firefox SQLite databases will
# not open using Python 2.7.6

import sqlite3
import sys
import os
import time

def run_tests():
	current_time = int(time.time() * 1000000 - 3600000000)
	print(current_time)
	user = os.environ.get(r"USERPROFILE")
	if user is None:
		print("Error: cannot access user's directory")
		exit(1)
	print("The following is a selection of things that might be interesting.")
	print("False positives may appear if non-private browsing used in last hour.")
	print()
		
	prefix = os.getenv(r"APPDATA", r"{user}\AppData\Roaming".format(user=user))
	path = r"{start}\Mozilla\Firefox\Profiles".format(start=prefix)
	for dirpath, dirnames, filenames in os.walk(path):
		for file in filenames:
			if file == "cookies.sqlite":
				print("\n---Cookies created in last hour---")
				print("If a user is currently using private browsing, cookies will show up here.")
				print("If a user terminated a private browsing session in the last hour, they may not.")
				db = os.path.join(dirpath, file)
				conn = sqlite3.connect(db)
				cursor = conn.cursor()
				cursor.execute("SELECT * FROM moz_cookies WHERE creationTime >= ?", (current_time,))
				print(cursor.fetchall())
			if file == "places.sqlite":
				print("\n---Places with unknown visit times---")
				print("Displays URLs with no last visit date but nonzero frequencies")
				print("Entries toward bottom of list are likely more recent.")
				db = os.path.join(dirpath, file)
				conn = sqlite3.connect(db)
				cursor = conn.cursor()
				# Why Firefox named this column "frecency", I have no idea...
				cursor.execute("SELECT url FROM moz_places WHERE frecency > 0 AND last_visit_date IS NULL")
				for item in cursor.fetchall():
					print(item[0])
				
	exit(0)

def interact():
	user = os.environ.get(r"USERPROFILE")
	if user is None:
		print("Error: cannot access user's directory")
		exit(1)
		
	searchpaths = []
	prefix = os.getenv(r"LOCALAPPDATA", r"{user}\AppData\Local".format(user=user))
	searchpaths.append("{start}\Mozilla\Firefox\Profiles".format(start=prefix))
	prefix = os.getenv(r"APPDATA", r"{user}\AppData\Roaming".format(user=user))
	searchpaths.append(r"{start}\Mozilla\Firefox\Profiles".format(start=prefix))

	# Finds available tables
	tables = []
	for path in searchpaths:
		for dirpath, dirnames, filenames in os.walk(path):
			for file in filenames:
				if file.endswith("sqlite"):
					db = os.path.join(dirpath, file)
					conn = sqlite3.connect(db)
					cursor = conn.cursor()
					try:
						cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
					except sqlite3.DatabaseError:
						print("Error reading", db)
					else:
						tables.append(cursor.fetchall())
					conn.close()
	
	finished = False
	while not finished:
		print("Type a table name to view its data.")
		for name in tables:
			print(name)
		choice = input("View table (or Q to quit): ")
		if choice == "Q":
			finished = True
			continue
		if choice not in tables:
			print("Error: Not a valid table.")
			continue
		else:
			print("Error: Not yet implemented.")
		# Realized that this doesn't associate table names with files. Hmm.

# Checks to be sure we're running on Windows with Python 3.3.3
if sys.platform != "win32":
	print("Error: This program runs on Windows.")
	exit(1)
version = sys.version_info
if (version.major, version.minor, version.micro) != (3, 3, 3):
	print("Warning: This program is designed for Python 3.3.3.")
	print("You are running:", version.major, ".", version.minor, ".", version.micro)

# Asks user to choose a mode
print("Choose a mode to run in:")
print("1. Show potential private browsing artifacts from last hour.")
print("2. Interactive mode")
choice = input("Enter 1 or 2: ")
if choice == "1":
	run_tests()
if choice == "2":
	interact()
else:
	print("Invalid choice.")
	exit(1)