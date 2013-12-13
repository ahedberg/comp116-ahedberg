# read_memory

# Reads memory maps of Mozilla Firefox and Google Chrome (while they are
# running) to look for private browsing artifacts

# Note: requires WinAppDbg 1.5 (http://winappdbg.sourceforge.net/Downloads.html)
# Note: runs using Python 2.7.6. WinAppDbg is not compatible with Python 3.3.3,
#       and it has no intention of becoming compatible with it.

from winappdbg import System, Process, CrashDump
import os

system = System()
executables = []
executables.append("firefox.exe")
executables.append("chrome.exe")


for task in system:
	task_name = task.get_filename()
	print task_name
	if task_name is None:
		continue
	if task_name.find("firefox.exe") is not -1:
		process = Process(task.get_pid())
		memory_map = process.get_memory_map()
		print CrashDump.dump_memory_map(memory_map)
	