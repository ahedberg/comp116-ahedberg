# read_browser_databases

# Processes on-disk SQLite database files for Mozilla Firefox and Google Chrome
# to search for private browsing artifacts

# Notes: Run using Python 3.3.3; some encrypted Firefox SQLite databases will
# not open using Python 2.7.6

import sqlite3
import os

user = os.environ.get(r"USERPROFILE")
if user is None:
	print("Error: cannot access user's directory")
	exit(1)
	
searchpaths = []
prefix = os.getenv(r"LOCALAPPDATA", r"{user}\AppData\Local".format(user=user))
searchpaths.append("{start}\Mozilla\Firefox\Profiles".format(start=prefix))
prefix = os.getenv(r"APPDATA", r"{user}\AppData\Roaming".format(user=user))
searchpaths.append(r"{start}\Mozilla\Firefox\Profiles".format(start=prefix))

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
					tables = cursor.fetchall()
					for name in tables:
						print(name[0])
						cursor.execute("SELECT sql FROM sqlite_master WHERE type='table' AND tbl_name=?;", name)
						print(cursor.fetchall())
						cursor.execute("SELECT * FROM {tablename}".format(tablename=name[0]))
						print(cursor.fetchone())
						print()
				conn.close()