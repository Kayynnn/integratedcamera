import cv2

cap = cv2.VideoCapture(1)


# path = '/run/user/1000/gvfs/mtp:host=Android_Android_1ed04da/Internal shared storage/DCIM/output.avi'
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('/media/rostugs/MIDIN/output.avi', fourcc, 30, (640,480))

while(True):
    ret, frame = cap.read()
    out.write(frame)
    cv2.imshow('frame', frame)
    c = cv2.waitKey(1)
    if c & 0xFF == ord('c'):
        cv2.imwrite('output.jpg', frame)

    if c & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()