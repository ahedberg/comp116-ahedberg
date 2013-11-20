# Assignment 5: Forensics

Ashley Hedberg and Tucker Stone

## Part 1
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

<!-- TODO look for more applications -->
4. The following applications are installed:
   * Burpsuite - found through looking at contents of /usr/bin

5. <!-- TODO root password-->

6. <!-- TODO additional user accounts -->

7. In the /root/Pictures directory, there are photos of Celine Dion. In
   /root/Documents, there are tracklists and tour dates for Celine Dion, as
   well.

8. <!-- TODO move or delete files -->

9. <!-- TODO encrypted files -->

10. Yes. According to the file receipt.pdf in /root, the suspect went to see
the celebrity in <!-- TODO open file and figure out what's up -->

11. <!-- TODO weird things with files on system -->

12. The suspect is stalking Celine Dion.

