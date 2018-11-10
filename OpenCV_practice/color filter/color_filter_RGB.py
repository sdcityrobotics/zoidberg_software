# Exactly the same as color_filter_HSV.py except we are using RGB ranges
# Note that this is much noisier!!!

# Highlights pixels that are within the RBG range for a red bouy

# '005.jpg' is an image of 3 different colored bouys in the water
# 'R_005.jpg' is a cropped image of the red bouy in '005.jpg'

# Summary of approach:
#   - Get a RGB range for a red bouy from 'R_005.jpg'
#   - Highlight all pixels in '005.jpg' that are within this RGB range

import cv2
import numpy as np
 
while(1):
    
   #Get a RGB range for a red bouy from 'R_005.jpg'
   crop =  cv2.imread('R_005.jpg', 1) 
   b,g,r = cv2.split(crop)
   
   lower_red = np.array([b.min()-5, g.min()-5, r.min()-5])
   upper_red = np.array([b.max()+5, g.max()+5, r.max()+5])
 
   #print RGB range
   print lower_red, upper_red
 
   #Highlight all pixels in '005.jpg' that are within this RGB range
   frame = cv2.imread('005.jpg', 1) 
   mask = cv2.inRange(frame, lower_red, upper_red)
   res = cv2.bitwise_and(frame,frame, mask= mask) 
 
   #erosion and dilation
   retval = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
   opening = cv2.morphologyEx(res, cv2.MORPH_OPEN, retval)
 
   #show images
   cv2.imshow('frame',frame) # '005.jpg'
   cv2.imshow('mask',mask) # mask of pixels within RGB range
   cv2.imshow('res',res) #show pixels in '005.jpg' with RGB range
   cv2.imshow('opening', opening) #show res after erosion and dilation
 
   cv2.waitKey(0)
   break
 
cv2.destroyAllWindows()
