# The Privacy of Private Browsing
By Ashley Hedberg  
Mentor: Ming Chow  
Tufts University Department of Computer Science  

## Contents
The following files are included with this project:
* paper.pdf - the paper in PDF format
* paper.tex - the paper in LaTeX markup. If the commits for paper.pdf and
  paper.tex are the same, they are probably equivalent
* read_browser_databases.py - reads the SQLite databases associated with
  Mozilla Firefox. Choice of pre-defined searches that may return a few 
  browser artifacts or a rudimentary interactive mode. Uses Python 3.3.3. To 
  be added:
  * Ability to view columns for tables and construct dynamic queries (using
  bind variables to prevent SQL injection attacks)
  * Google Chrome support
* read_memory.py - reads strings stored in memory of Mozilla Firefox and Google
  Chrome processes. Prints strings to terminal window. Uses Python 2.7.6. To 
  be added:
  * Writing all strings to a log file and additionally printing interesting
  strings (such as those containing URLs) to terminal window
  * Access in-memory SQLite database
  