Submitted By
============
Ashley Hedberg  
Comp 116 Assignment 1: Packet Sleuth  
9/17/2013 11:59 pm

set1.pcap
=========
1. There are 276 packets in this set.

2. FTP (file transfer protocol) was used to transfer these files from the PC to
   the server.

3. FTP is insecure because passwords are sent in the clear. Nothing is
   encrypted using FTP. Packet 15 contains the user's password.

4. The secure alternative to FTP is FTPS, which uses SSL to encrypt data
   transmitted over the network. (Source: [Understanding Key Differences
   Between FTP, FTPS, and SFTP](http://www.jscape.com/blog/bid/75602/Understanding-Key-Differences-Between-FTP-FTPS-and-SFTP))

5. The IP address of the server is 67.23.79.113.

6. The username and password used to access the server are as follows:
    * username: stokerj
    * password: w00tfu!

7. Three files were transferred from PC to server.

8. The names of the files transferred from PC to server are as follows:
    * code.rtf
    * secret.pdf
    * abc.jpg

9. Three files with the same names as above were extracted by following the
   TCP stream of the FTP-DATA packets after each STOR request.



set2.pcap
=========
10. There are 74566 packets in this set.

11. There are 9 plaintext username-password pairs in this packet set.

12. Username-password pairs were discovered by filtering the packet set by
    insecure protocols using Wireshark. FTP, Telnet, Rlogin, rsh, POP, SMTP, 
    SNMP, NFS, and IMAP were searched. For each protocol, each TCP stream was 
    viewed to look for usernames and passwords. Streams were then filtered out
    of view so that all packets for that protocol would eventually be 
    inspected.

    Domain names were found using nslookup.

13. Plaintext username-password pairs found:

<table>
  <tr>
    <th>Username</th>
    <th>Password</th>
    <th>Protocol</th>
    <th>Server IP</th>
    <th>Domain Name</th>
    <th>Destination Port Number</th>
  </tr>
  <tr>
    <!-- invalid -->
    <td>cisco</td>
    <td>185 chris10</td>
    <td>Telnet</td>
    <td>200.60.17.1</td>
    <td></td>
    <td>23</td>
  </tr>
  <tr>
    <!-- invalid -->
    <td>cisco</td>
    <td>185 chelita</td>
    <td>Telnet</td>
    <td>200.60.17.1</td>
    <td></td>
    <td>23</td>
  </tr>
  <tr>
    <!-- invalid -->
    <td>cisco</td>
    <td>185 chayank</td>
    <td>Telnet</td>
    <td>200.60.17.1</td>
    <td></td>
    <td>23</td>
  </tr>
  <tr>
    <!-- invalid -->
    <td>cisco</td>
    <td>185 cereza</td>
    <td>Telnet</td>
    <td>200.60.17.1</td>
    <td></td>
    <td>23</td>
  </tr>
  <tr>
    <!-- not sure... -->
    <td>cisco</td>
    <td>185 buburuza</td>
    <td>Telnet</td>
    <td>200.60.17.1</td>
    <td></td>
    <td>23</td>
  </tr>
  <tr>
    <!-- invalid -->
    <td>e129286</td>
    <td>4.Ekkama</td>
    <td>POP3</td>
    <td>144.122.144.179</td>
    <td>arikanda.general.services.metu.edu.tr</td>
    <td>110</td>
  </tr>
  <tr>
    <!-- valid -->
    <td>mbergeson@hjnews.com</td>
    <td>mb123on</td>
    <td>POP3</td>
    <td>67.128.149.178</td>
    <td>mail.newswest.com</td>
    <td>110</td>
  </tr>
  <tr>
    <!-- valid -->
    <td>brewer</td>
    <td>1qazxsw209simona12</td>
    <td>POP3</td>
    <td>62.173.185.22</td>
    <td>imartini.it</td>
    <td>110</td>
  </tr>
  <tr>
    <!-- valid -->
    <td>dmartini@cutaway.it</td>
    <td>se1lasa</td>
    <td>IMAP</td>
    <td>109.168.119.166</td>
    <td></td>
    <td>143</td>
  </tr>
</table>
