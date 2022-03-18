import os
import ftplib
import time

server = 'telematics.transtrack.id'
user = '15874661a9be9feafb0'
password = 'b193a4a95ef9fb64'

while True:
    if os.path.isfile('queue.txt'):
        f = open('queue.txt')
        lines = f.read()

        print("Read queue.txt :", lines)
        ftp = ftplib.FTP(server, user, password)
        imgname = lines.strip()
        print(imgname)
        if os.path.isfile(imgname):     
           img = open(imgname, 'rb')
           ftp.storbinary('STOR '+imgname, img)
           os.remove(imgname)
        ftp.quit()
        os.remove('queue.txt')
        open('mulai_interval.txt', 'w+')
        print("dah beres")
        time.sleep(10)

    print("waiting....")
