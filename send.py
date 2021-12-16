import os
import ftplib

server = 'telematics.transtrack.id'
user = '15874661a9be9feafb0'
password = 'b193a4a95ef9fb64'

while True:
    if os.path.isfile('queue.txt'):
        with open('queue.txt') as f:
            lines = f.readlines()
                       
        ftp = ftplib.FTP(server, user, password)
        for z in lines:
            print(z.strip())
            if os.path.isfile(z.strip()):     
             f = open(z, 'rb')
             ftp.storbinary('STOR '+imgname[z], f)
        ftp.quit()
        os.remove('queue.txt')
