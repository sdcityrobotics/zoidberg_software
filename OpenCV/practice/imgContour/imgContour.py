import cv2
import numpy as np

# '2d-circle.png', 'oval.png', 'balloons.jpg'
img = cv2.imread('balloons.jpg', 1)

# blur functions
blurred_frame = cv2.GaussianBlur(img, (5, 5), 0)
hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)

# based heavily on color for images, change RGB bounds
lower_blue = np.array([50, 50, 50])
upper_blue = np.array([140, 255, 255])
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# for findContours
image, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# find and draw contours if found
for contour in contours:
    area = cv2.contourArea(contour)

    # draw contour if area is large enough`
    if area > 1000:
        cv2.drawContours(img, contour, -1, (0, 255, 0), 3)

# display
cv2.imshow("img", img)
cv2.imshow("mask", mask)

cv2.waitKey(0)
cv2.destoryAllWindows()
