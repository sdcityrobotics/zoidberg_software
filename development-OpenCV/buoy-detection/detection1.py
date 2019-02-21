import numpy as np
import cv2
#from matplotlib import pyplot

# images for testing:
# from comp's video: '001.png', '002.png', '003.png', 004.png', '005.png'
# external buoy's: '010.jpg', ...
img = cv2.imread('002.png', 0)
img_color = cv2.imread('002.png')

# import sobel function to convert image (derivative WRT y)
# ksize value influences noise levels
sobel_y = cv2.Sobel(img, cv2.CV_8U, 0, 1, ksize = 5)

# functions to heighten contour detection, changed number of iterations
thresh_y = cv2.threshold(sobel_y, 200, 255, cv2.THRESH_BINARY)[1]
thresh_y = cv2.erode(thresh_y, None, iterations = 1)
thresh_y = cv2.dilate(thresh_y, None, iterations = 1)

######### Finding which contours are buoys #########
contours = cv2.findContours(thresh_y.copy(), cv2.RETR_EXTERNAL, cv2. CHAIN_APPROX_SIMPLE)
contours = contours[1];

ratioMax = 2.0
ratioMin = 0.5

buoys = []
count = 0 
for contour in contours:
   if (len(contour) > 20):
      #find the highest point in y (will have the lowest valie at [0])
      highestPt = [9999999, 9999999] #set to be just really high
      endPt1 = [0, 9999999999] #will be pt with lowest [1]
      endPt2 = [0,-1] #will be pt with highest [1]
    
      for Point in contour:
         tempy = Point[0][0]
         tempx = Point[0][1]
         if (tempy < highestPt[0]):
            highestPt = Point[0]
         if (tempx < endPt1[1]):
            endPt1 = Point[0]
         if (tempx > endPt2[1]):
            endPt2 = Point[0]

      print('endPoint1', endPt1)
      print('endPoint2', endPt2)
      print('highestPt', highestPt)

      #pick the endpoint highest in y (so lowest [0]
      finalEndPt = endPt1;
      if (endPt1[0] > endPt2[0]):
         finalEndPt = endPt2;

      w = abs(highestPt[1] - finalEndPt[1])
      h = abs(highestPt[0] - finalEndPt[0])
      if (w != 0):
         ratio = (h/(2*w))
      else: #safeguard against dividing by 0
         ratio = 0
      if (endPt1[0]==endPt2[0] and endPt1[1]==endPt2[1]):
         ratio = 0

      print('ratio', ratio)
      print()
      if ((ratio > ratioMin) and (ratio < ratioMax)):
         print('valid ratio: ', ratio)
         buoys.append(contour)
         count = count+1

print('total valid ratios: ', count)
#print('valid contours: ', buoys)

# display
for buoy in buoys:
   cv2.drawContours(img_color, [buoy], -1, (255, 255, 0), 2)
cv2.imshow('Contours', img_color)

cv2.waitKey(0)
cv2.destroyAllWindows()                                                                                                                                                           1,1           Top
