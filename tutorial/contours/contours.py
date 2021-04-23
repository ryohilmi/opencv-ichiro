import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import os

image_path = os.path.join(os.getcwd(), 'images', 'contours.jpg')
image = cv.imread(image_path)

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(gray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

biggest_contour = max(contours, key=lambda item: item.size)
biggest_contour_index = contours.index(biggest_contour)
biggest_contour_parent = contours[hierarchy[0][biggest_contour_index][3]]

cv.drawContours(image, (biggest_contour, biggest_contour_parent), -1, (0, 255, 0), 3)

plt.subplot(121), plt.imshow(image)
plt.subplot(122), plt.imshow(thresh, cmap='gray')
plt.show()

