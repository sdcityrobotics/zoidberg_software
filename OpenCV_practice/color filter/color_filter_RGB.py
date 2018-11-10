# Highlights pixels that are within the hue light saturation (HSV) range for a red bouy

# '005.jpg' is an image of 3 different colored bouys in the water
# 'R_005.jpg' is a cropped image of the red bouy in '005.jpg'

# Summary of approach:
#   - Get a HSV range for a red bouy from 'R_005.jpg'
#   - Highlight all pixels in '005.jpg' that are within this HSV range

import cv2
import numpy as np
 
while(1):
    
   #Hue Saturation Value
   crop =  cv2.imread('R_005.jpg', 1) 
   
   b,g,r = cv2.split(crop)
   lower_red = np.array([b.min()-5, g.min()-5, r.min()-5])
   upper_red = np.array([b.max()+5, g.max()+5, r.max()+5])
 
   print lower_red, upper_red
 
   frame = cv2.imread('005.jpg', 1) 
   mask = cv2.inRange(frame, lower_red, upper_red)
   res = cv2.bitwise_and(frame,frame, mask= mask) 
 
   #erosion and dilation
   retval = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
   opening = cv2.morphologyEx(res, cv2.MORPH_OPEN, retval)
 
   #show images
   #cv2.imshow('frame',frame)
   cv2.imshow('mask',mask)
   #cv2.imshow('res',res)
   #cv2.imshow('opening', opening)
 
   cv2.waitKey(0)
   break
 
cv2.destroyAllWindows()
