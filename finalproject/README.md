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
  browser artifacts or a rudimentary interactive mode. Uses Python 3.3.3.
  Potential extensions:
  * Ability to view columns for tables and construct dynamic queries (using
  bind variables to prevent SQL injection attacks)
  * Google Chrome support
* read_memory.py - reads strings stored in memory of Mozilla Firefox and Google
  Chrome processes. Prints strings containing http:// or https:// to terminal 
  window and logs all strings to an output file. Output for Firefox and Chrome
  are stored separately in case of both browsers running concurrently. Uses 
  Python 2.7.6. Potential extensions:
  * Filter out bookmarks and hyperlinks contained in loaded pages
  * Access in-memory SQLite database (URI location unknown, if one exists)
  