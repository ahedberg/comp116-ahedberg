# read_browser_databases

# Processes on-disk SQLite database files for Mozilla Firefox and Google Chrome
# to search for private browsing artifacts

# Notes: Run using Python 3.3.3; some encrypted Firefox SQLite databases will
# not open using Python 2.7.6

import sqlite3
import os

# hard-coded search path - find environment variable
searchpaths = []

searchpaths.append(r"C:\Users\Ashley\AppData\Local\Mozilla\Firefox\Profiles")
searchpaths.append(r"C:\Users\Ashley\AppData\Roaming\Mozilla\Firefox\Profiles")

for path in searchpaths:
	for dirpath, dirnames, filenames in os.walk(path):
		for file in filenames:
			if file.endswith("sqlite"):
				db = os.path.join(dirpath, file)
				conn = sqlite3.connect(db)
				cursor = conn.cursor()
				try:
					cursor.execute("SELECT name FROM sqlite_master;")
				except sqlite3.DatabaseError:
					print("Error reading", db)
				conn.close()
