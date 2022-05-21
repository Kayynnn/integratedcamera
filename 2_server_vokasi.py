import RPi.GPIO as GPIO
import os
import cv2
import time
from PIL import Image
import math
from pytz import HOUR, timezone
from datetime import datetime

#GPIO Set Up
GPIO.setmode(GPIO.BCM) 
GPIO.setup(18,GPIO.IN) #gpio 18, pin 12

#login credentials ftp
server = 'telematics.transtrack.id'
user = '15874661a9be9feafb0'
password = 'b193a4a95ef9fb64'

import subprocess
x = ""

# while x == "":
#   x = subprocess.check_output("ls ./", shell=True)
#   x = str(x.strip()).strip("b\'")
#   print(x)

# video time stamp
date = datetime.now()
tz = timezone("Etc/GMT+7")
date = date.replace(tzinfo=tz)

# video format and save
format = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('./'+x+'/cam_'+str(date)+'.avi', format, 15, (640,480))

# checks the first 10 indexes.
index = 0
arr = []
i = 10
while i > 0:
    cap = cv2.VideoCapture(index)
    # ret, frame = cap.read()
    if cap.read()[0]:
        arr.append(index)
        # cv2.imshow('frame', frame)
        # time.sleep(5)
        cap.release()
    index += 1
    i -= 1
print(arr)

# camera id
cam = cv2.VideoCapture(arr[0])

# make sure theres no extra files when starting program
if os.path.isfile('mulai_interval.txt'):
      os.remove('mulai_interval.txt')
os.system("sudo rm -f *.jpg")

do = "jalan"
interval = 0

mqtt_interval = 1

while(True):

  #gpio read
  gpio_trigger = GPIO.input(18)
  # firebase get interval
  if os.path.isfile("interval.txt"): 
     f = open('interval.txt')
     mqtt_interval =  int(f.read())


  # getting camera frames
  ret, frame = cam.read()
  # video write
  out.write(frame)
  
  if do == "jalan" or interval >= mqtt_interval*15 or gpio_trigger:
    #timestamp
    date = datetime.now()
    tz = timezone("Etc/GMT+7")
    date = date.replace(tzinfo=tz)

    # naming image files based on camera and timestamp
    imgname = "cam_"+str(date)+".jpg"
                #"cam2_"+str(date)+".jpg"]
                # "cam3_"+str(date)+".jpg",
                # "cam4_"+str(date)+".jpg"]    

    # writing images
    cv2.imwrite(imgname, frame)
   
    # resizing the image
    foo = Image.open(imgname)
    x, y = foo.size
    mult = 1.5
    x2, y2 = math.floor(x*mult), math.floor(y*mult)
    foo = foo.resize((x2,y2),Image.ANTIALIAS)
    foo.save(imgname,optimize=True, quality=50)
    
    # making queue file for sending
    with open('queue.txt', 'w+') as f:
      f.write(imgname)
        
    if gpio_trigger != 1:
      interval = 0
      do = "  "
      do2 = "mulai interval" 
      if os.path.isfile('mulai_interval.txt'):
            os.remove('mulai_interval.txt')    
    
    
    # getting the interval time after sending
    

  # timer start
  if do2 == "mulai interval" and os.path.isfile('mulai_interval.txt'):
    start = time.perf_counter()
    do2 = "  " 
  # timer ends
  if os.path.isfile('mulai_interval.txt'):
    end = time.perf_counter()
    interval = (end - start)
    print(interval)
    print(gpio_trigger)
