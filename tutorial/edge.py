import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

threshold_min = 100
threshold_max = 200

image = cv.imread('images/cat.png', 0)

def print_image():
  edge_img = cv.Canny(image, threshold_min, threshold_max)

  plt.subplot(121), plt.imshow(image, cmap='gray')
  plt.title('Original'), plt.xticks([]), plt.xticks([])

  plt.subplot(122), plt.imshow(edge_img, cmap='gray')
  plt.title('Edge ({}, {})'.format(threshold_min, threshold_max)), plt.xticks([]), plt.xticks([])

  plt.show()

def on_min_trackbar(val):
  global threshold_min;
  threshold_min = val;
  print_image()
  
def on_max_trackbar(val):
  global threshold_max;
  threshold_max = val;
  print_image()

window = 'Threshold'
cv.namedWindow(window)
cv.namedWindow(window)

min_threshold = 'Min threshold'
cv.createTrackbar(min_threshold, window, threshold_min, 400, on_min_trackbar)

max_threshold = 'Max threshold'
cv.createTrackbar(max_threshold, window, threshold_max, 400, on_max_trackbar)

print_image()

cv.waitKey(0) & 0xFF  
cv.destroyAllWindows()

