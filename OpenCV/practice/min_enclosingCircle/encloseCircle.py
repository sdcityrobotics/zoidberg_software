import numpy as np
import cv2

# not finding center accurately in 3D-images
img = cv2.imread('2d-circle.png', 0)
og = cv2.imread('2d-circle.png', 0)

cv2.imshow('original', og)

# use threshold, findContours and moment functions
ret, thresh = cv2.threshold(img, 127, 255, 0)
im2, contours, hierarchy = cv2.findContours(thresh, 1, 2)
cont = contours[0]

# use data to edit center and radius
moment = cv2.moments(cont)
print(moment)

# find center using minEnclosingCircle
(x, y), radius = cv2.minEnclosingCircle(cont)

# for printing/drawing
center = (int(x), int(y))
radius = int(radius)
cv2.circle(img, center, radius, (0, 255, 0), 10)

# for reference
print ("center = " +  str(center))
print("radius = (" + str(x) + ", " + str(y) + ")")

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
