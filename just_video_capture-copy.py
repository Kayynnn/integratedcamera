import cv2

cam1 = cv2.VideoCapture(3)
# cam2 = cv2.VideoCapture(1)

# video format and save
format = cv2.VideoWriter_fourcc(*'VXID')
out1 = cv2.VideoWriter('output.avi', format, 24, (640,480))
# out2 = cv2.VideoWriter('output2.avi', format, 24, (640,480))

while(True):
  # video frames
  retv1, framev1 = cam1.read() 
  # retv2, framev2 = cam2.read()

  # video write
  out1.write(framev1)
  # out2.write(framev2)