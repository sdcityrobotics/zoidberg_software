import numpy as np
import cv2

img = cv2.imread('2d-circle.png', 0)
og = cv2.imread('2d-circle.png', 0)

ret, thresh = cv2.threshold(img,127,255,0)
im2, contours, hierarchy = cv2.findContours(thresh, 1, 2)

# defining how to find/use moment
cnt = contours[0]
M = cv2.moments(cnt)

# calculating centroid(x, y) and area from M
cx = int(M['m10'] / M['m00'])
cy = int(M['m01'] / M['m00'])
area = cv2.contourArea(cnt)

# drawing circle at centroid
cv2.circle(img, (cx, cy), 30, (0, 255, 0,), -1)

print("center of x = " + str(cx))
print("center of y = " + str(cy))
print("contour area = " + str(area))

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destoryAllWindows()
