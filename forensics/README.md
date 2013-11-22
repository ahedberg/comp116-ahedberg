# Assignment 5: Forensics

Ashley Hedberg and Tucker Stone

## Part 1
Firstly, diff was run to compare each file against the others. b.jpg and c.jpg
were found to be the same, but a.jpg was different from both of them.

The following was run for each of the provided .jpg files: steghide extract -sf
[filename]

When the passphrase prompt appeared, the enter key was pressed (using the empty
string "" as the passphrase). For files b.jpg and c.jpg, no data could be
extracted using that passphrase. However, for file a.jpg, the file prado.jpg 
was extracted. a.jpg contained a photo of Norman Ramsey hidden inside a photo 
of Norman Ramsey.

<!-- It should be noted that this was overheard by a particular classmate 
*cough* Nicholas Andre *cough* who was talking a bit too loudly about his
forensics work in 111. Seemed silly not to try it. Worked like a charm! -->

## Part 2
1. This SD card has two partitions:
   * A Win95 FAT32 partition (sectors 1 to 125001)
   * A Linux partition (sectors 125001 to 15398839)

2. There does not appear to be a phone carrier involved.

3. The Kali Linux 1.0 operating system is being used. This was determined by
   opening the /etc/\*\_version file. On this SD card, it was named
   /etc/debian\_version.

4. The following applications are installed. Autospy was used to browse through
   the SD card's filesystem.
   * Burpsuite - found through looking at contents of /usr/bin
   * Metasploit - found in /opt folder
   * Wireshark - found in /etc folder
   * Unicorn Scan - found in /etc folder; similar to nmap
   * Tor - found in /etc folder
   * Ice Weasel - found in /etc folder; web browser
   <!-- TODO look for more applications -->

5. Yes. The root password is "toor". This was discovered by running John the
   Ripper against the passwd and shadow files recovered using Autospy against
   many wordlists. The ipmi\_passwords.txt wordlist cracked the password.

6. We do not believe that there are additional user accounts on the system. The
   /home folder contains no other user directories, which we would expect to
   see.

7. In the /root/Pictures directory, there are photos of Celine Dion. In
   /root/Documents, there are tracklists and tour dates for Celine Dion, as
   well.

8. The suspect tried to delete files before his arrest. Autospy revealed
   several indications of recently deleted files:

9. <!-- TODO encrypted files -->

10. Yes. According to the file receipt.pdf in /root, the suspect went to see
    Celine Dion at the Colosseum at Caesars Palace in Las Vegas, NV on July
    28, 2012. The ticket was sold to Ming Chow.
   <!-- TODO open file and figure out what's up -->

11. <!-- TODO weird things with files on system -->

12. The suspect is stalking Celine Dion.

