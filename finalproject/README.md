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
  Mozilla Firefox (Google Chrome to be added). Choice of pre-defined
  searches that may return a few browser artifacts or a rudimentary
  interactive mode. Uses Python 3.3.3.
* read_memory.py - attempts to read the in-memory SQLite databases
  associated with Mozilla Firefox (Google Chrome to be added). Currently
  achieves a memory map of the process and freezes spectacularly. Uses
  Python 2.7.6.