import os
#import ftplib
import cv2
import time
from PIL import Image
import math
import firebase_admin
from firebase_admin import credentials,db 
from pytz import HOUR, timezone
from datetime import datetime

# export credential key
ced = credentials.Certificate("ya.json")

# initiliaze realtime database
default_app = firebase_admin.initialize_app(ced, {'databaseURL': 'https://integratedcamera-36d77-default-rtdb.firebaseio.com'})
ref = db.reference('interval')

# login credentials
server = 'telematics.transtrack.id'
user = '15874661a9be9feafb0'
password = 'b193a4a95ef9fb64'



# video format and save
format = cv2.VideoWriter_fourcc(*'XVID')
out1 = cv2.VideoWriter('output.avi', format, 15, (640,480))
out2 = cv2.VideoWriter('output2.avi', format, 15, (640,480))

cam1 = cv2.VideoCapture(0)
cam2 = cv2.VideoCapture(2)

# server login and send
# def send(s, u, p):
#   ftp = ftplib.FTP(s, u, p)
#   for z in range(2):
#     f = open(imgname[z], 'rb')
#     ftp.storbinary('STOR '+imgname[z], f)
#   ftp.quit()

# #def pict_capture():
#   # saving the images
#   cv2.imwrite(imgname[0], frame1)
#   cv2.imwrite(imgname[1], frame2)

#   # resizing the image
#   for i in range(2): 
#     foo = Image.open(imgname[i])
#     x, y = foo.size
#     mult = 1.5
#     x2, y2 = math.floor(x*mult), math.floor(y*mult)
#     foo = foo.resize((x2,y2),Image.ANTIALIAS)
#     foo.save(imgname[i],optimize=True, quality=50)

#   # send to server with interval in seconds
#   send(server, user, password)

# scheduling time
#schedule.every(3).seconds.do(pict_capture)


do = "jalan"
interval = 0
while(True):
  # firebase get interval
  try:
    fbinterval = ref.get() 
  except:
    print("Cant get the interval")

  # getting camera frames
  ret1, frame1 = cam1.read()
  ret2, frame2 = cam2.read()

  # video write
  out1.write(frame1)
  out2.write(frame2)
  

  if do == "jalan" or interval >= fbinterval*30:
    #timestamp
    date = datetime.now()
    tz = timezone("Etc/GMT+7")
    date = date.replace(tzinfo=tz)

    # naming image files based on camera and timestamp
    imgname = [ "./pictures/cam1_"+str(date)+".jpg",
                "./pictures/cam2_"+str(date)+".jpg"]
                # "cam3_"+str(date)+".jpg",
                # "cam4_"+str(date)+".jpg"]    

    cv2.imwrite(imgname[0], frame1)
    cv2.imwrite(imgname[1], frame2)

    # resizing the image
    for i in range(2): 
      foo = Image.open(imgname[i])
      x, y = foo.size
      mult = 1.5
      x2, y2 = math.floor(x*mult), math.floor(y*mult)
      foo = foo.resize((x2,y2),Image.ANTIALIAS)
      foo.save(imgname[i],optimize=True, quality=50)
    
    with open('queue.txt', 'w+') as f:
        for x in imgname:
            f.write(x)
            f.write('\n')

    interval = 0    
    #start = time.perf_counter()
    # send to server with interval in seconds
    # send(server, user, password)

    do = "  "
    do2 = "mulai interval"
    if os.path.isfile('mulai_interval.txt'):
      os.remove('mulai_interval.txt')
  if do2 == "mulai interval" and os.path.isfile('mulai_interval.txt'):
    start = time.perf_counter()
    do2 = "  "     
  if os.path.isfile('mulai_interval.txt'):
    end = time.perf_counter()
    interval = (end - start)
    print(interval)     
  # 
  #schedule.run_pending()