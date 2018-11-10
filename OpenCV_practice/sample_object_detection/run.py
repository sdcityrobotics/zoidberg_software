import numpy as np
import cv2
 
import vision

name_of_image = '005.jpg'
 
img = cv2.imread(name_of_image,1)  
#cv2.imshow('before image', img)
 
my_test = vision.VisionTasks()
biggestObject = my_test.findBiggestObject(img); #(image, shape, cX, cY)
 
cv2.imshow('Biggest Object in Image', biggestObject[0])
cv2.waitKey(0)
cv2.destroyAllWindows()
