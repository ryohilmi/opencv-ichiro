import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

image = cv.imread('images/duaribu.jpg')

h, w = image.shape[:2]

points1 = np.float32([[250,580],[3490,590], [50, 2005], [3600,2070]])
points2 = np.float32([[0,0], [4000, 0], [0, 2250], [4000, 2250]])

M = cv.getPerspectiveTransform(points1, points2)

res = cv.warpPerspective(image, M, (w, h))

plt.subplot(121),plt.imshow(image), plt.title('Input')
plt.subplot(122),plt.imshow(res), plt.title('Output')
plt.show()