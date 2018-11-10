import cv2
import numpy as np 
 
while(1):
    
   #Hue Saturation Value
   crop =  cv2.imread('R_005.jpg', 1) 
   hsv = cv2.cvtColor(crop, cv2.COLOR_BGR2HSV)
    
   h, s, v = cv2.split(hsv)
   
   #b,g,r = cv2.split(crop)
   #lower_red = np.array([b.min()-5, g.min()-5, r.min()-5])
   #upper_red = np.array([b.max()+5, g.max()+5, r.max()+5])
 
   #for this example: [ 9 114 226] [ 19 159 255]
   lower_red = np.array([h.min()-5, s.min()-5, v.min()-5])
   upper_red = np.array([h.max()+5, s.max()+5, v.max()+5])
 
   print lower_red, upper_red
 
   frame = cv2.imread('005.jpg', 1) 
   hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
   mask = cv2.inRange(hsv, lower_red, upper_red)
   res = cv2.bitwise_and(frame,frame, mask= mask) 
 
   #erosion and dilation
   retval = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
   opening = cv2.morphologyEx(res, cv2.MORPH_OPEN, retval)
 
   #show images
   cv2.imshow('frame',frame)
   cv2.imshow('mask',mask)
   #cv2.imshow('res',res)
   #cv2.imshow('opening', opening)
 
   cv2.waitKey(0)
   break
 
cv2.destroyAllWindows()
