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

11. 
