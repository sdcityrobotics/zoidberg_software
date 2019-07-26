#!/usr/bin/env python

#a class that determines the shape of the biggest contour

import cv2
import numpy as np
from shape_detector import ShapeDetector
 
class VisionTasks:
     
   def findBiggestObject(self, image):
      #Consider resizing image
      #Resizing image to a smaller factor can help better approximate shapes
     
      #Process Image. Setting the second arg to True will display dilation
      processedImage = self.preProcessImage(image, True)
      
      #Find the biggest contour in the processed image
      #Returns an array of points that make up the biggest contour
      contour = self.findBiggestContour(processedImage)
       
      #Detect the shape of the biggest contour
      sd = ShapeDetector() #create instance of the ShapeDetector class
      shape, approx = sd.detect(contour) #returns the determined shape and an array with the contour vertices
       
      #Compute the center of the contour
      M = cv2.moments(contour)
      cX = int((M["m10"] / M["m00"]))
      cY = int((M["m01"] / M["m00"]))
  
      #Add contour and text to the image
      contour = contour.astype("int")
      cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)
      cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
         0.5, (255, 255, 255), 2)
       
      #Add contour vertices to the image
      red = [0,0,255]
      for pix in approx:
         pix1 = pix[0][0]
         pix2 = pix[0][1]
         cv2.circle(image, (pix1, pix2), 3, red, 2) 
      
      #return the image with shape information, the shape name, and the center of the contour
      return (image, shape, cX, cY) 
    
   def preProcessImage(self, image, showDilation):
      "Process the Image"

      #thresholds
      th1 = 0
      th2 = 200
 
      blurred = cv2.blur(image, (3, 3))
      kernel = np.ones((3, 3), np.uint8)
      erosion = cv2.erode(blurred, kernel, iterations=1) #removes noise
      edges = cv2.Canny(erosion, th1, th2)
 
      dilation = cv2.dilate(edges, kernel, iterations=2) #enhances remaining features
      if showDilation:
         cv2.imshow("dilation", dilation)
       
      return dilation
        
   def findBiggestContour(self, mask):
      "Returns the biggest contour"
      contoursArray = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
      
      # This code will execute if at least one contour was found
      if len(contoursArray) > 0:
         # Find the biggest contour
         biggestContour = max(contoursArray, key=cv2.contourArea)
         # Returns an array of points for the biggest contour found
         return biggestContour
   
   #not used in findBiggestObject()
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

      return (image, centerX, centerY, w)
 
   #not used in findBiggestObject()
   def detectCircles(self, gray):
      "Use cv2.HoughCircles to find and show detected circles"
      circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 3)
 
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
