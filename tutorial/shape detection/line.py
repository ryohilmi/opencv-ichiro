import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

image = cv.imread('images/sudoku.jpg')
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray, 50, 150, apertureSize=3)

lines = cv.HoughLines(edges, 1, np.pi / 180, 150)

for line in lines:
  rho,theta = line[0]
  a = np.cos(theta)
  b = np.sin(theta)
  x0 = a*rho
  y0 = b*rho
  x1 = int(x0 + 1000*(-b))
  y1 = int(y0 + 1000*(a))
  x2 = int(x0 - 1000*(-b))
  y2 = int(y0 - 1000*(a))
  
  cv.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

plt.imshow(image)
plt.show()