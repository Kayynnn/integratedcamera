import cv2
import time
def returnCameraIndexes():
    # checks the first 10 indexes.
    index = 0
    arr = []
    i = 10
    while i > 0:
        cap = cv2.VideoCapture(index)
        if cap.read()[0]:
            arr.append(index)
            cap.release()
        index += 1
        i -= 1
    print(arr)
    cam1 = cv2.VideoCapture(arr[0])
    # cam2 = cv2.VideoCapture(arr[1])
    # while True:
    #     ret, frame = cam1.read()
    #     ret2, frame2 = cam2.read()
    #     cv2.imshow('frame', frame)
    #     cv2.imshow('frame2', frame2)
    # # time.sleep(10)
    # # return arr
    #     c = cv2.waitKey(1)
    #     if c & 0xFF == ord('q'):
    #         break
    cam1.release()
    cam2.release()
    cv2.destroyAllWindows()
returnCameraIndexes()