import cv2
import time
def returnCameraIndexes():
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
    # return arr

returnCameraIndexes()