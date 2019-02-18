import numpy as np
import cv2

# 'soccer-goal-plain.jpg', 'blackbox.jpg'
img = cv2.imread('goalpost.jpg', 0)

# using Sobel (WRT x) derivative to find edges
sobelx_8U = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize = 5)
sobelx_64F = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize = 5)

# more functions to find edges better?

# convert the 64F image to be able to imshow
abs_sobelx_64F = np.absolute(sobelx_64F)
sobel_64F_convert = np.uint8(abs_sobelx_64F)

cv2.imshow('img', img)
cv2.imshow('sobelx_8U', sobelx_8U)
cv2.imshow('sobelx_64F', sobelx_64F)

cv2.waitKey(0)
cv2.destroyAllWindows()
