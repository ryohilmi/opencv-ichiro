import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import os

image_path = os.path.join(os.getcwd(), 'images', 'xp.jpg')
image = cv.imread(image_path)

color = ['b', 'g', 'r']

for i, col in enumerate(color):
  hist = cv.calcHist([image], [i], None, [256], [0, 255])
  plt.plot(hist, color=col)
  plt.xlim([0, 256])

plt.show()
