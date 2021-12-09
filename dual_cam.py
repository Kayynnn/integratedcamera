import cv2
import time

cam1 = cv2.VideoCapture(0)
cam2 = cv2.VideoCapture(2)
x = 0

while (True):
    ret1, frame1 = cam1.read()
    ret2, frame2 = cam2.read()

    # cv2.imshow('cam1', frame1)
    # cv2.imshow('cam2', frame2)

    # if cv2.waitKey(10) & 0xFF == ord('c'): 
    time.sleep(3)
    x = x + 1
    cv2.imwrite('cam1_'+str(x)+'.png', frame1)
    cv2.imwrite('cam2_'+str(x)+'.png', frame2)