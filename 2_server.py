import os
import ftplib
import cv2
import time
from PIL import Image
import math

server = 'telematics.transtrack.id'
user = '15874661a9be9feafb0'
password = 'b193a4a95ef9fb64'

cam = cv2.VideoCapture(0)

def sizing(i):
  foo = Image.open(i)
  x, y = foo.size
  mult = 0.4
  x2, y2 = math.floor(x*mult), math.floor(y*mult)
  foo = foo.resize((x2,y2),Image.ANTIALIAS)
  foo.save("4-1.png",quality=100)  

def send(s, u, p):
  ftp = ftplib.FTP(s, u, p)
  f = open('4-1.png', 'rb')
  ftp.storbinary('STOR 4-1.png', f)
  ftp.quit()

ret, frame = cam.read()
time.sleep(1)
cv2.imwrite('4.png', frame)

img = './4.png'
size = os.path.getsize(img)

sizing(img)
send(server, user, password)

# capture >> resize >> sending