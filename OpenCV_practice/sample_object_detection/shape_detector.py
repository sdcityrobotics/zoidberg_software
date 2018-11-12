#A class that determines the shape of a given contour
#The current options are: tirangle, square, rectangle, pentagon, and circle

import cv2
 
class ShapeDetector:
   def __init__(self):
      pass
 
   def detect(self, c):
      shape = "unidentified"
       
      #compute the perimeter of the contour
      peri = cv2.arcLength(c, True) 
       
      #contour approximation
      #retuns an array of 'vertices' that make up the contour
      approx = cv2.approxPolyDP(c, 0.02*peri, True)
      print "contour approx", approx
 
      #The number of vertices are used to determine the shape
      if len(approx) == 3:
         shape = "triangle"
      
      elif len(approx) == 4:
         (x, y, w, h) = cv2.boundingRect(approx)
         ar = w/ float(h)
          
         shape = "square" if ar >= 0.95 and ar <= 1.05 else "rectangle"
       
      elif len(approx) == 5:
         shape = "pentagon"
 
      else:
         shape = "circle"
 
      #return both the shape (as a string) and the array of vertices
      return (shape, approx)
