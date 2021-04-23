import cv2 as cv
import numpy as np
import os

image_path = os.path.join(os.getcwd(), 'images', 'beach.jpg')
image = cv.imread(image_path, 0)
image = cv.resize(image, (400, 400))

equ = cv.equalizeHist(image)
res = np.hstack((image, equ))

cv.imshow('Result', res)
cv.waitKey(0)
cv.destroyAllWindows()