import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('images/bluered.jpg')

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

kernel = np.ones((5, 5), np.uint8)

lower_red = np.array([160, 50, 50])
upper_red = np.array([180, 255, 255])

lower_blue = np.array([100, 50, 50])
upper_blue = np.array([120, 255, 255])

red_mask = cv.inRange(hsv, lower_red, upper_red)
blue_mask = cv.inRange(hsv, lower_blue, upper_blue)

red_mask =  cv.morphologyEx(red_mask, cv.MORPH_GRADIENT, kernel)

contours, hierarchy = cv.findContours(blue_mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

contours_img = blue_mask.copy()

print(contours)

cv.drawContours(contours_img, contours, -1, (0, 255, 0), 3)

plt.subplot(221), plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
plt.subplot(222), plt.imshow(red_mask, cmap='gray')
plt.subplot(223), plt.imshow(blue_mask, cmap='gray')
plt.subplot(224), plt.imshow(contours_img)

plt.show()