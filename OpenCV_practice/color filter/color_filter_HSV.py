# Highlights pixels that are within the hue light saturation (HSV) range for a red bouy

# '005.jpg' is an image of 3 different colored bouys in the water
# 'R_005.jpg' is a cropped image of the red bouy in '005.jpg'

# Summary of approach:
#   - Get a HSV range for a red bouy from 'R_005.jpg'
#   - Highlight all pixels in '005.jpg' that are within this HSV range

import cv2
import numpy as np 
 
while(1):

   # Get a HSV range for a red bouy from 'R_005.jpg'
   crop =  cv2.imread('R_005.jpg', 1)
   hsv = cv2.cvtColor(crop, cv2.COLOR_BGR2HSV)
   h, s, v = cv2.split(hsv)
 
   lower_red = np.array([h.min()-5, s.min()-5, v.min()-5])
   upper_red = np.array([h.max()+5, s.max()+5, v.max()+5])
 
   #Print the HSV range
   print lower_red, upper_red
 
   #Highlight all pixels in '005.jpg' that are within this HSV range
   frame = cv2.imread('005.jpg', 1) 
   hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
   mask = cv2.inRange(hsv, lower_red, upper_red) #mask of pixels within this HSV range
   res = cv2.bitwise_and(frame,frame, mask= mask)  #the final result
 
   #erosion (reduce noise) and dilation (make resulting structures in the image bigger)
   retval = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
   opening = cv2.morphologyEx(res, cv2.MORPH_OPEN, retval)
 
   #show images
   cv2.imshow('frame',frame) # '005.jpg'
   cv2.imshow('mask',mask) # mask of pixels within HSV range
   cv2.imshow('res',res) # show pixels in '005.jpg' within HSV range
   cv2.imshow('opening', opening) #show res after erosion and dilation
 
   cv2.waitKey(0)
   break
 
cv2.destroyAllWindows()
