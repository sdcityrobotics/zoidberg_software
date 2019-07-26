import cv2
from findObjects import findObjects

cap = cv2.VideoCapture('yellow_buoy.mov')
divideFrameBy = 4

while(cap.isOpened()):
   ret, frame = cap.read()
   height, width, channel = frame.shape

   #uncomment to flip the frame
   #timg = cv2.transpose(frame)
   #timg = cv2.flip(timg,flipCode=1)

   #uncomment to resize the frame
   #THIS HELPS IMAGE DETECTION 
   #NOTE this will change the standard output
   frame = cv2.resize(frame, (int(width / divideFrameBy), int(height / divideFrameBy)))

   [standard_output, marked_image] = findObjects(frame)
   print(standard_output)
   
   cv2.imshow('frame', marked_image)
   if cv2.waitKey(2) & 0xFF == ord('q'):
      break

cap.release()
cv2.destroyAllWindows()

