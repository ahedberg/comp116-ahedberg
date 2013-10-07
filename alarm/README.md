Assignment 2: Incident Alarm
============================

## Functionality ##
This program analyzes a stream of network packets for several incidents:

1. *NULL scan* - Alerts that an incident has occurred when all TCP flags equal 0. This is known to detect
    incidents correctly.
2. *Xmas scan* - Alerts that an incident has occurred when URG, PSH, and FIN TCP flags equal 1. This is
    known to detect incidents correctly.
3. *Other Nmap scans* - Alerts that an incident has occurred when the payload of a TCP packet contains the    string "Nmap".
4. *Password leakage* - Alerts that an incident has occurred when the payload of a packet contains the
    string "PASS".
5. *Credit card number leakage* - Alerts that an incident has occurred when the regular expression
    described by SANS (link below) is matched.
6. *Basic cross-site scripting* - Alerts that an incident has occurred when the payload of a packet
    contains the strings "&lt;script&gt;" and "alert". This test is highly susceptible to false positives, as 
    plenty of websites that are not vulnerable to cross-site scripting would send packets containing both
    of these strings.

## TODO List ##
* Test other Nmap scans - determine which flags put Nmap in payload
* Serve dummy webpage to test cases 4-6

## Sources ##
I discussed this assignment with Tyler Lubeck and with classmates on Piazza. In addition, I used the following sources:
  * [String Search in Ruby](http://ruby-doc.org/core-2.0.0/String.html#method-i-include-3F)
  * [Using Snort to Detect Credit Card Numbers](http://www.sans.org/security-resources/idfaq/snort-detect-credit-card-numbers.php)
