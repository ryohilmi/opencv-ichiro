import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import os

image_path = os.path.join(os.getcwd(), 'images', 'cat.png')
image = cv.imread(image_path, 0)

img = cv.medianBlur(image, 5)

ret, thresh1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
thresh2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
thresh3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)


titles = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, thresh1, thresh2, thresh3]

for i in range(4):
  plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')
  plt.title(titles[i])
  plt.xticks([]), plt.yticks([])

plt.show()