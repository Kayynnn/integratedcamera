import schedule
# import time
import cv2
from PIL import Image
import math
from pytz import HOUR, timezone
from datetime import datetime


format = cv2.VideoWriter_fourcc(*'XVID')
out1 = cv2.VideoWriter('output.avi', format, 30, (640,480))

cam1 = cv2.VideoCapture(1, cv2.CAP_DSHOW)

def capture_img():
    cv2.imwrite(imgname[0], frame1)

    for i in range(1): 
        foo = Image.open(imgname[i])
        x, y = foo.size
        mult = 1.5
        x2, y2 = math.floor(x*mult), math.floor(y*mult)
        foo = foo.resize((x2,y2),Image.ANTIALIAS)
        foo.save(imgname[i],optimize=True, quality=50)


# def job():
    
    
schedule.every(3).seconds.do(capture_img)
# schedule.every().minutes.do(job)
# schedule.every().hour.do(job)

while True:
    try:
        interval = 1#ref.get() 
    except:
        print("Cant get the interval")
    
    #timestamp
    date = datetime.now()
    tz = timezone("Etc/GMT+7")
    date = date.replace(tzinfo=tz)
    
    # getting camera frames
    ret1, frame1 = cam1.read()
    
    # show the frames
    # cv2.imshow('vid1', frame1)
    # cv2.imshow('vid2', frame2)

    try:
    # naming image files based on camera and timestamp
        imgname = [ "cam1_"+str(date)+".jpg"]
    except:
        print("Error")

        break
    out1.write(frame1)
    schedule.run_pending()
    # time.sleep(1)