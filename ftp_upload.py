# username -- password -- interval waktu
# from picamera import PiCamera # error : no module named picamera
from ftplib import FTP
import ftplib
import os
import time
import datetime
import cv2

# camera = cv2.VideoCapture(0)
# camera = PiCamera(0)

# Depends on how your camera is set up...my Pi is turned sideways
# camera.rotation = 270
# camera.hflip = True

# Load FTP server credentials
try:
    upload_ftp = os.getenv('telematics.transtrack.id')
    upload_user = os.getenv('15874661a9be9feafb0')
    upload_password = os.getenv('b193a4a95ef9fb64')
except:
    raise Exception('Environmental variables with FTP info cannot be loaded')

# ret,frame = camera.read()

ftp = FTP(upload_ftp, upload_user, upload_password)

x = 1
# And run forever
while True:
    time.sleep(2)
    # t = datetime.datetime.utcnow().hour
    # Save bandwidth by not uploading during very night times
    # if ((t - 7) > 5) or ((t - 7) < 1):
    if x == 1:
        # cv2.imwrite('1.png',frame)
        # camera.capture('/tmp/cam.jpg')
        try:
            f = open('1.png', 'r')

            # First we upload the image to a temporary name, then rename it on the server.
            # This prevents someone loading the image online as corrupted during upload.
            ftp.storbinary('STOR 1.png', f)
            ftp.rename('1.png', '1.1.png')

        except Exception as e:
            print('Exception: %s' % (e))
            try:
                ftp.quit()
                ftp = FTP(upload_ftp, upload_user, upload_password)
            except Exception as f:
                print('Error, %s and %s' % (e, f))
        time.sleep(5)
    else:
        print('Not uploading during night time.')
        time.sleep(60)
    