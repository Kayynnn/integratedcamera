import os
import ftplib
from ftplib import FTP
import cv2
import time
from PIL import Image
import math
import firebase_admin
from firebase_admin import credentials,db 
#export credential key
ced = credentials.Certificate("ya.json")

# In the above line <path_to_generated_private_key>
# is a placeholder for the generate JSON file containing
# your private key.

#initiliaze realtime database
default_app = firebase_admin.initialize_app(ced, {'databaseURL': 'https://integratedcamera-36d77-default-rtdb.firebaseio.com'})
ref = db.reference('interval')
interval = ref.get()

try:
  server = 'telematics.transtrack.id'
  user = '15874661a9be9feafb0'
  password = 'b193a4a95ef9fb64'
except:
  raise Exception('Environmental variables with FTP info cannot be loaded')

ftp = FTP(server,user,password)

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
  
  

while(True):
  time.sleep(interval*5)
  ret, frame = cam.read()
  cv2.imwrite('4.png', frame)

  img = './4.png'
  size = os.path.getsize(img)

  sizing(img)

  try:
    send(server, user, password)
  except Exception as e:
    print('Exception: %s' % (e))
    
    try:
      ftp.quit()
      ftp = FTP(server,user,password)
    except Exception as f:
      print('Error, %s and %s' % (e, f))
  time.sleep(5)

# capture >> resize >> sending
