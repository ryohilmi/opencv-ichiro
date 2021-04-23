import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import os

image_path = os.path.join(os.getcwd(), 'images', 'dompet.png')
image = cv.imread(image_path, 0)

ret, thresh = cv.threshold(image, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, 1, 2)

