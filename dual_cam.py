import os
import ftplib
import cv2
import time
from PIL import Image
import math
import firebase_admin
from firebase_admin import credentials,db 

# ced = credentials.Certificate("ya.json")

# default_app = firebase_admin.initialize_app(ced, {'databaseURL': 'https://integratedcamera-36d77-default-rtdb.firebaseio.com'})
# ref = db.reference('interval')
# interval = ref.get()

# server = 'telematics.transtrack.id'
# user = '15874661a9be9feafb0'
# password = 'b193a4a95ef9fb64'

cam1 = cv2.VideoCapture(0)
cam2 = cv2.VideoCapture(1)
x = 0

while (True):
    ret1, frame1 = cam1.read()
    ret2, frame2 = cam2.read()

    cv2.waitKey(5000)   
    x = x + 1
    cv2.imwrite('cam1_'+str(x)+'.png', frame1)
    cv2.imwrite('cam2_'+str(x)+'.png', frame2)