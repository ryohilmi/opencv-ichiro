import numpy as np
import cv2 as cv
import os

img = cv.imread('images/circles.jpg', 0)
img = cv.medianBlur(img, 5)
cimg = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)

                            
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    cv.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
    cv.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)
    
cv.imshow('Detected Circles',cimg)
cv.waitKey(0)
cv.destroyAllWindows()