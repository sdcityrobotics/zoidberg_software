import numpy as np
import cv2
import datetime

def findObjects(img):
   #timestamp taken before image processing
   sTimeStamp = str(datetime.datetime.now()) #string timestamp
   #add this to the standard output
   standard_output = sTimeStamp

   #img = cv2.imread(img_text, 0)
   #img_color = cv2.imread(img_text)
   
   img_color = img.copy()
   img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

   # import sobel function to convert image (derivative WRT y)
   # ksize value influences noise levels
   sobel_y = cv2.Sobel(img, cv2.CV_8U, 0, 1, ksize = 5)

   # functions to heighten contour detection, changed number of iterations
   thresh_y = cv2.threshold(sobel_y, 200, 255, cv2.THRESH_BINARY)[1]
   thresh_y = cv2.erode(thresh_y, None, iterations = 1)
   thresh_y = cv2.dilate(thresh_y, None, iterations = 1)
   
   #cv2.imshow('filter', thresh_y)

   ######### Finding which contours are buoys #########
   contours = cv2.findContours(thresh_y.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
   contours = contours[1];

   ratioMax = 0.5
   ratioMin = 0.2

   buoys = []
   count = 0
   for contour in contours:
      #cv2.drawContours(img_color, [contour], -1, (255, 255, 0), 2)
      if (len(contour) > 45):
         #find the highest point in y
         highestPt = [9999999, 9999999] #set to be just really high
         endPt1 = [9999999999, 0] #will be pt with lowest x
         endPt2 = [-1, 0] #will be pt with highest x
   
         for Point in contour:
            tempy = Point[0][1]
            tempx = Point[0][0]
            if (tempy < highestPt[1]):
               highestPt = Point[0]
            if (tempx < endPt1[0]):
               endPt1 = Point[0]
            if (tempx > endPt2[0]):
               endPt2 = Point[0]
   
         #pick the endpoint highest in y
         finalEndPt = endPt1;
         if (endPt1[1] > endPt2[1]):
            finalEndPt = endPt2;
   
         w = abs(highestPt[0] - finalEndPt[0])
         h = abs(highestPt[1] - finalEndPt[1])
         if (w != 0):
            ratio = (h/(2*w))
         else: #safeguard against dividing by 0
            ratio = 0
   
         if ((ratio >= ratioMin) and (ratio <= ratioMax)):
            #print('finalEndPt', finalEndPt)
            #print('highestPt', highestPt)
            #print('valid ratio: ', ratio)
            #print()
            buoys.append(contour)
            count = count+1
   
   #print('total valid ratios: ', count)
   
   for buoy in buoys:
      (x,y),radius = cv2.minEnclosingCircle(buoy)
      #y = y + 11
      center = (int(x), int(y))
      radius = int(radius)
   
      # Removing contours that are actually noise
      q = (radius*1)/4 #arbitary distance from the center
      outliers = 0; #number of points in an unexpected location
      for point in buoy:
         point = point[0]
         #if the pointis below the center of the circle (in y)
         #and within q pixels of the center in x, then it is an outlier 
         if (point[1] > center[1] and (point[0] > center[0] - q and point[0] < center[0]+q)): 
            outliers = outliers + 1
      print('outliers: ', outliers)
      #print('radius: ', radius, '\n')
      if (outliers > 1): #if a contour has too many outliers, it's noise
         continue
   
      #uncomment this to draw contours and encolsing circle
      #cv2.drawContours(img_color, [buoy], -1, (255, 255, 0), 2)
      #img_color = cv2.circle(img_color, center, radius, (0, 255, 0), 2)
   
      #drawing rectangle around circle for labeling
      cv2.rectangle(img_color, (int(x) + radius, int(y)+ radius), (int(x) - radius, int(y) - radius), (255, 0, 0), 2)

      cv2.putText(img_color, str(int(x)) + ', ' + str(int(y)), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX,
         0.5, (0, 0, 0), 2)

      #print("center(x, y) = (" + str(x) + ", " + str(y) + ")")
      #print("radius = " + str(radius))
      standard_output = standard_output + ", " + "001, " + str(int(x)) + ", " + \
         str(int(y)) + ", " + str(radius*2) + ", " + str(radius*2)

   #print("center - (x, y) = (" + str(x) + ", " + str(y) + ")")
   

   #return standard_output, image
   return [standard_output, img_color]
   
      
