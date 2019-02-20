import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('sample-gate.png', 0)

blurred = cv2.blur(img, (3, 3))
thresh = cv2.threshold(blurred, 100, 200, cv2.THRESH_BINARY)[1]
erosion = cv2.erode(thresh, None, iterations = 2)
edges = cv2.Canny(thresh, 100, 200)

cv2.imshow('img', img)
cv2.imshow('edges', edges)

cv2.waitKey(0)
cv2.destoryAllWindows()
