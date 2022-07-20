# Writeup for "0ld is g0ld" challenge from Hack The Box
## This is a challenge about cracking a pdf, we have a pdf called "0ld is g0ld.pdf" but we dont know the password

# Solution:
First, i tried to use hashcat to crack the pdf, using file command we can check that this is a pdf version 1.6
![pdfformat](img/pdfformat.png)
however, after tryng to use hashcat for a while i found a tool that is called pdfcrack, so...
[ppdfcrack](img/ppdfcrack.png)d
this gives us that the result is 
