#Run this script to find the shape of the biggest contour

import numpy as np
import cv2
 
import vision

name_of_image = 'balloon.jpg'
 
img = cv2.imread(name_of_image,1)  
#cv2.imshow('before image', img)
 
my_test = vision.VisionTasks() #create an instance of the class

#returns the image with the shape drawn, the shape name, and the center of the shape
biggestObject = my_test.findBiggestObject(img); # (image, shape, cX, cY)

#display this image
cv2.imshow('Biggest Object in Image', biggestObject[0])
cv2.waitKey(0)
cv2.destroyAllWindows()
