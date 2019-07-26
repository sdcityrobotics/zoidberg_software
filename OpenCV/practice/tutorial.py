import numpy as np
import cv2
 
img = cv2.imread('sample.jpg',0)
cv2.imshow('image',img)
k = cv2.waitKey(0)
cv2.destroyAllWindows()
