# Python program to explain cv2.putText() method
    
# importing cv2
import cv2

# Reading an image in default mode
image = cv2.imread('.\geeks14.png')
  
# font
font = cv2.FONT_HERSHEY_SIMPLEX
  
# org
org = (50, 50)
  
# fontScale
fontScale = 1
   
# Blue color in BGR
color = (255, 0, 0)
  
# Line thickness of 2 px
thickness = 2
   
# Using cv2.putText() method
image = cv2.putText(image, 'OpenCV', org, font, 
                   fontScale, color, thickness, cv2.LINE_AA)
   
# Displaying the image
cv2.imshow('image', image) 
cv2.imwrite('output.jpg',image)