import numpy as np
import cv2
from matplotlib import pyplot

# images for testing:
# from comp's video: '001.png', '002.png', '003.png', 004.png', '005.png'
# external buoy's: '010.jpg', ...
img = cv2.imread('002.png', 0)

# import sobel function to convert image (derivative WRT y)
# ksize value influences noise levels
sobel_y = cv2.Sobel(img, cv2.CV_8U, 0, 1, ksize = 5)
sobelNoise = cv2.Sobel(img, cv2.CV_8U, 0, 1, ksize = 7)

# functions to heighten contour detection, changed number of iterations
thresh_y = cv2.threshold(sobel_y, 200, 255, cv2.THRESH_BINARY)[1]
thresh_y = cv2.erode(thresh_y, None, iterations = 1)
thresh_y = cv2.dilate(thresh_y, None, iterations = 1)

threshNoise = cv2.threshold(sobelNoise, 200, 255, cv2.THRESH_BINARY)[1]
threshNoise = cv2.erode(threshNoise, None, iterations = 2)
threshNoise = cv2.dilate(threshNoise, None, iterations = 2)

# display
cv2.imshow('Sobel Y', thresh_y)
cv2.imshow('Sobel-Noisy', threshNoise)

# for reference, display array of contours
# contours = cv2.findContours(thresh_y.copy(), cv2.RETR_EXTERNAL, cv2. CHAIN_APPROX_SIMPLE)
# print(contours)

cv2.waitKey(0)
cv2.destroyAllWindows()
