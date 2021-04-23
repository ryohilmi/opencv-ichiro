import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('images/cat.png', 0)
img2 = img.copy()
template = cv.imread('images/cat_head.png', 0)
h, w = template.shape[:2]

img = img2.copy()

res = cv.matchTemplate(img,template,cv.TM_CCOEFF)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)

cv.rectangle(img,top_left, bottom_right, 255, 2)
plt.subplot(121), plt.imshow(res, cmap='gray')
plt.title('Matching Result'), plt.xticks([]), plt.yticks([])

plt.subplot(122),plt.imshow(img,cmap = 'gray')
plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
plt.suptitle('TM_CCOEFF')

plt.show()