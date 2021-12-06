import os
import ftplib
import glob

ftp = ftplib.FTP('telematics.transtrack.id','15874661a9be9feafb0','b193a4a95ef9fb64')

for image in glob.glob(os.path.join('2.png')):
  with open(image, 'rb') as file:
    ftp.storbinary('STOR 2.png', file)

ftp.quit()