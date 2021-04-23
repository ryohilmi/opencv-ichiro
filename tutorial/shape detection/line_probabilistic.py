import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

image = cv.imread('images/sudoku.jpg')
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray, 50, 150, apertureSize=3)

lines = cv.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=10)
for line in lines:
    x1,y1,x2,y2 = line[0]
    cv.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
    
plt.imshow(image)
plt.show()