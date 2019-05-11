import numpy as np
import cv2
	
img_text = 'img5.png'
img = cv2.imread(img_text)
original = img

# (50, 100) works well with 4 and 5 
# too noisy for everything else
# (100, 200) works well with 1, 2, 3
# not with 4 and 5
min_value = 50
max_value = 100

# draw image and return coordinates of drawn pixels
image = cv2.Canny(img, min_value, max_value)
indices = np.where(image != 0)
coordinates = zip(indices[1], indices[0])

# iterate through coordinates to see if there were any found
pt_count = 0
pt_threshold = 5

# draw points
for point in coordinates:
	cv2.circle(img, point, 1, (0, 0, 255), -1)
	#print(point)
	
cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

# PHASE 1: (currently here)
# will eventually iterate through image
# if no points were found in coordinates, 
# min and max value will be halved, then
# will iterate through image once more
# until enough coordinates are found

# PHASE 2: (tentative plans)
# (a)
# since the buoy will always have somewhat of a rectangular shape, 
# collect the two farthest x-coordinates in a certain threshold, 
# find the center, then look vertically to find any noise
# (b) or simply draw detected 'rectangle'

# (c)
# collect all lines horizontally from coordinates,
# find center of line
# then look down x amount of pixels
# if drawn pixels are found AKA noise, 
# throw the potential detection out

# PHASE 3: 
# functionalize everything
