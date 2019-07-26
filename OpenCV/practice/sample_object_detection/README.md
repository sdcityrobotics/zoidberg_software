To run this:
--------------
`python run.py`

What it does
-------------
It finds the biggest contour in the object, then uses cv2.approxPolyDP() to find the vertices that make up the contour. Depending on the number of vertices found, a shape is determined. For example, if the number of vertices are greater than 5, the biggest contour is classified as a circle. The image is displayed with the biggest contour in green and its vertices in red. The name of the determined shape is also displayed on the image.
