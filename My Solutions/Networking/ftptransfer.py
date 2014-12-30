'''

Created For Mega Projects Repository

FTP Program - A file transfer program which can transfer files back and forth
from a remote web sever.

@author: Sambit

'''

from ftplib import FTP

ftp = FTP('domainname.com')
ftp.login(user='username', passwd='password')
ftp.cwd('/specificdomain-or-location/')

# Grab the file from the server and write it to a local file.
def grabFile():
    filename = 'fileName.txt'
    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
    ftp.quit()
    localfile.close()

#Upload a file to the server
def placeFile():
    filename = 'fileName.txt'
    ftp.storbinary('STOR '+filename, open(filename, 'rb'))
    ftp.quit()
