import os
import ftplib
import cv2
import time
from PIL import Image
import math
import firebase_admin
from firebase_admin import credentials,db 
from pytz import HOUR, timezone
from datetime import datetime
import time

# export credential key
ced = credentials.Certificate("ya.json")

# initiliaze realtime database
default_app = firebase_admin.initialize_app(ced, {'databaseURL': 'https://integratedcamera-36d77-default-rtdb.firebaseio.com'})
ref = db.reference('interval')

# login credentials
server = 'telematics.transtrack.id'
user = '15874661a9be9feafb0'
password = 'b193a4a95ef9fb64'

# server login and send
def send(s, u, p):
  ftp = ftplib.FTP(s, u, p)
  for z in range(2):
    f = open(imgname[z], 'rb')
    ftp.storbinary('STOR '+imgname[z], f)
  ftp.quit()

while(True):
  # capture wait
  # cv2.waitKey(5000)
  try:
    interval = ref.get() 
  except:
    print("Cant get the interval")
  # camera id
  try:
    cam1 = cv2.VideoCapture(0)
    cam2 = cv2.VideoCapture(1)
  except:
    print("Camera Error")
  #timestamp
  date = datetime.now()
  tz = timezone("Etc/GMT+7")
  date = date.replace(tzinfo=tz)
  
  # getting camera frames
  ret1, frame1 = cam1.read()
  ret2, frame2 = cam2.read()
  
  # naming image files based on camera and timestamp
  imgname = [ "cam1_"+str(date)+".png",
              "cam2_"+str(date)+".png",
              "cam3_"+str(date)+".png",
              "cam4_"+str(date)+".png"]  

  # saving the images
  cv2.imwrite(imgname[0], frame1)
  cv2.imwrite(imgname[1], frame2)

  # release after capture image
  cam1.release()
  cam2.release()

  # resizing the image
  for i in range(2): 
    foo = Image.open(imgname[i])
    x, y = foo.size
    mult = 1
    x2, y2 = math.floor(x*mult), math.floor(y*mult)
    foo = foo.resize((x2,y2),Image.ANTIALIAS)
    foo.save(imgname[i],optimize=True, quality=0.1)

  # send to server with interval in seconds
  send(server, user, password)
  time.sleep(interval*3)
  # test