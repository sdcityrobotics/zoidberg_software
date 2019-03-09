import cv2 
from findObjects import findObjects

# images for testing:
# from comp's video: '001.png', '002.png', '003.png', 004.png', '005.png'
# external buoy's: '010.jpg', ...
img_text = '005.png'
img = cv2.imread(img_text)

#find objects in a frame
[standard_output, marked_image] = findObjects(img)

cv2.imshow('Contours', marked_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
