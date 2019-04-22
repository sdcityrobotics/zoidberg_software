import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    # blur
    blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)
    hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)

    # range (based on color --> tweak RGB values)
    lower_range = np.array([40, 90, 0])
    upper_range = np.array([120, 255, 255])
    mask = cv2.inRange(hsv, lower_range, upper_range)

    # find contours
    _, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    # calculate area for each contours
    for contour in contours:
        area = cv2.contourArea(contour)

        # tweak value for more/less sens
        if area > 5000:
            cv2.drawContours(frame, contour, -1, (0, 255, 0), 3)

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    key = cv2.waitKey(1)
    if key == 2:
        break

cap.release()
cv2.destroyAllWindows()
