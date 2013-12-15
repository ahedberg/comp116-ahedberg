# read_memory
# read_memory

# Reads memory maps of Mozilla Firefox (while they are
# running) to look for private browsing artifacts

# Note: requires WinAppDbg 1.5 (http://winappdbg.sourceforge.net/Downloads.html)
# Note: runs using Python 2.7.6. WinAppDbg is not compatible with Python 3.3.3,
#       and it has no intention of becoming compatible with it.

from winappdbg import System, Process, CrashDump, HexDump
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

system = System()
#executables = []
#executables.append("firefox.exe")
#executables.append("chrome.exe")


for task in system:
    task_name = task.get_filename()
    if task_name is None:
        continue
    if task_name.find("firefox.exe") != -1:
        process = Process(task.get_pid())
        #memory_map = process.get_memory_map()
		
		# Convert this to logging of some sort
		# And only print URL-like things?
        for address, size, data in process.strings():
            print HexDump.address(address), HexDump.printable(data)
    