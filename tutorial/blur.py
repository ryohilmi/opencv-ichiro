import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('images/cat.png')

averageBlur = cv.blur(img, (5, 5))
gaussianBlur = cv.GaussianBlur(img, (5, 5), 0)

plt.subplot(221),plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB)),plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(222),plt.imshow(cv.cvtColor(averageBlur, cv.COLOR_BGR2RGB)),plt.title('Averaging')
plt.xticks([]), plt.yticks([])

plt.subplot(223),plt.imshow(cv.cvtColor(gaussianBlur, cv.COLOR_BGR2RGB)),plt.title('Gaussian')
plt.xticks([]), plt.yticks([])

plt.show()