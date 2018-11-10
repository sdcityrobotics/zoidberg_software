#!/usr/bin/env python
import cv2
import numpy as np
from shape_detector import ShapeDetector
 
class VisionTasks:
     
   def findBiggestObject(self, image):
      #resize image to a smaller factor so that the shapes
      #can be better approximated
      #resized = imutils.resize(image, width=300)
      #ratio = image.shape[0] / float(resized.shape[0])
      
      #image = resized
      resized = image
      ratio = 1
  
      #Pre-process Image
      processedImage = self.preProcessImage(resized, True) #display dilatoin
 
      self.detectCircles(processedImage)
 
      #Find the biggest contour
      contour = self.findBiggestContour(processedImage)
       
      #Detect the shape of the biggest contour
      sd = ShapeDetector()
      shape, approx = sd.detect(contour)
       
      #Compute the center of the contour
      M = cv2.moments(contour)
      cX = int((M["m10"] / M["m00"]))
      cY = int((M["m01"] / M["m00"]))
  
      #Add contour and text to the image
      contour = contour.astype("float")
      #contour *= ratio
      contour = contour.astype("int")
      cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)
      cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
         0.5, (255, 255, 255), 2)
       
      #Add polyfit points on image
      red = [0,0,255]
      for pix in approx:
         pix1 = pix[0][0]
         pix2 = pix[0][1]
         cv2.circle(image, (pix1, pix2), 3, red, 2) 
 
      return (image, shape, cX, cY) 
    
   def preProcessImage(self, image, showDilation):
      "Preprocess the image"
      th1 = 0
      th2 = 200
 
      blurred = cv2.blur(image, (3, 3))
      kernel = np.ones((3, 3), np.uint8)
      erosion = cv2.erode(blurred, kernel, iterations=1)
      edges = cv2.Canny(erosion, th1, th2)
 
      dilation = cv2.dilate(edges, kernel, iterations=2)
      if showDilation:
         cv2.imshow("dilation", dilation)
       
      return dilation
        
   def findBiggestContour(self, mask):
      "Returns the biggest contour"
      contoursArray = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
      #print "len(contoursArray)", len(contoursArray)
      #print "contoursArray[0]", contoursArray[0]
      #print "contoursArray[1]", contoursArray[1]
      # This code will execute if at least one contour was found
      if len(contoursArray) > 0:
         # Find the biggest contour
         biggestContour = max(contoursArray, key=cv2.contourArea)
         # Returns an array of points for the biggest contour found
         return biggestContour
 
   def boundRectangle(self, contour):
      "Fits a rectagle around the biggest contour"
      x, y, w, h = cv2.boundingRect(contour)
      centerX = x + (w / 2)
      centerY = y + (h / 2)
      if centerX == 0 or centerY == 0 or w == 0:
         centerX = -1
         centerY = -1
         w = -1
      font = cv2.FONT_HERSHEY_SIMPLEX
      cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
      cv2.putText(image, "X: " + format(centerX), (int(x) - 60, int(y) + 50), font, 0.5, (155, 250, 55), 2,
             cv2.LINE_AA)
       
      cv2.putText(image, "Y: " + format(centerY), (int(x) - 60, int(y) + 70), font, 0.5, (155, 255, 155), 2,
            cv2.LINE_AA)
      # display
      return (image, centerX, centerY, w)
 
   def detectCircles(self, gray):
      # detect circles in the image
      circles = cv2.HoughCircles(gray, cv2.cv.CV_HOUGH_GRADIENT, 1, 3)
 
      # ensure at least some circles were found
      if circles is not None:
         # convert the (x, y) coordinates and radius of the circles to integers
         circles = np.round(circles[0, :]).astype("int")
 
         # loop over the (x, y) coordinates and radius of the circles
         for (x, y, r) in circles:
            # draw the circle in the output image, then draw a rectangle
            # corresponding to the center of the circle
            cv2.circle(output, (x, y), r, (0, 255, 0), 4)
            cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
 
            # show the output image
            cv2.imshow("output", np.hstack([image, output]))
            cv2.waitKey(0)
      else:
         print 'No circles found.'
