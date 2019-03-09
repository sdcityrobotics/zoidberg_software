import cv2
from findObjects import findObjects

cap = cv2.VideoCapture(0)
divideFrameBy = 4

ret, frame = cap.read()
height, width, channel = frame.shape

while(True):
   ret, frame = cap.read()
   frame = cv2.resize(frame, (int(width / divideFrameBy), int(height / divideFrameBy)))
   #find objects in a frame
   [standard_output, marked_image] = findObjects(frame)
   print(standard_output)
   
   cv2.imshow('frame', marked_image)
   if cv2.waitKey(1) & 0xFF == ord('q'):
      break

cap.release()
cv2.destroyAllWindows()

