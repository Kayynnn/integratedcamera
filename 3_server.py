import os
import ftplib
import cv2
import time

cam = cv2.VideoCapture(0)

server = 'telematics.transtrack.id'
user = '15874661a9be9feafb0'
password = 'b193a4a95ef9fb64'

ftp = ftplib.FTP(server, user, password)

# from pytz import timezone
# from datetime import datetime

# while(True):
    
    # date = datetime.now()
    # tz = timezone("Etc/GMT+7")
    # date = date.replace(tzinfo=tz)    
ret, frame = cam.read() 
time.sleep(1)
cv2.imwrite('4.png', frame)
f = open('4.png', 'rb')
ftp.storbinary('STOR 4.png', f)    

ftp.quit()