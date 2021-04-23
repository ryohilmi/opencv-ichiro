import cv2 as cv
import numpy as np
import os

img_path = os.path.join(os.getcwd(), 'images')

roi = cv.imread(os.path.join(img_path, 'xp-roi.jpg'))
hsv = cv.cvtColor(roi, cv.COLOR_BGR2HSV)

target = cv.imread(os.path.join(img_path, 'xp.jpg'))
hsvt = cv.cvtColor(target, cv.COLOR_BGR2HSV)

roihist = cv.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

cv.normalize(roihist, roihist, 0, 255, cv.NORM_MINMAX)
dst = cv.calcBackProject([hsvt], [0, 1], roihist, [0, 180, 0, 256], 1)

disc = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
cv.filter2D(dst, -1, disc, dst)

ret, thresh = cv.threshold(dst, 50, 255, 0)
thresh = cv.merge((thresh, thresh, thresh))
res = cv.bitwise_and(target, thresh)

res = np.vstack((target, thresh, res))
cv.imwrite('images/res.jpg', res)


