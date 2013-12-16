# read_memory

# Reads memory maps of Mozilla Firefox and Google Chrome (while they are
# running) to look for private browsing artifacts

# Note: requires WinAppDbg 1.5 (http://winappdbg.sourceforge.net/Downloads.html)
# Note: runs using Python 2.7.6. WinAppDbg is not compatible with Python 3.3.3,
#       and it has no intention of becoming compatible with it.

from winappdbg import System, Process, HexDump
import os
import sys

# Checks to be sure we're running on Windows with Python 2.7.6
if sys.platform != "win32":
    print("Error: This program runs on Windows.")
    exit(1)
version = sys.version_info
if (version.major, version.minor, version.micro) != (2, 7, 6):
    print("Error: This program is written for Python 2.7.6")
    print("You are running:", version.major, ".", version.minor, ".", version.micro)
    exit(1)

# Retrieves system snapshot and iterates through running tasks
system = System()
for task in system:
    task_name = task.get_filename()
    if task_name is None:
        continue
    if (task_name.find("firefox.exe") != -1) or (task_name.find("chrome.exe") != -1):
		# Obtains memory information about currently running browser
        process = Process(task.get_pid())   
        filename = ""
        if task_name.find("firefox.exe") != -1:
            filename = "firefox_output.txt"
        else:
            filename = "chrome_output.txt"
        with open(filename, "w") as f:
			# Extracts all string literals from memory
			# All strings are logged, while URLs are printed to terminal
            for address, size, data in process.strings():
                tuple = (HexDump.address(address), HexDump.printable(data))
                f.write(str(tuple))
                if tuple[1].startswith((r"http://", r"https://")):
                    print tuple
