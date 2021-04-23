import cv2 as cv
import numpy as np

img = cv.imread('images/xp.jpg')

h, w = img.shape[:2]

angle = int(input("Rotation angle : "))

M = cv.getRotationMatrix2D(((w-1)/2.0, (h-1)/2.0), angle, 1)
res = cv.warpAffine(img, M, (w,h))

cv.imshow('Image', img)
cv.imshow('Rotated', res)

k = cv.waitKey(0)
if k == ord('s'):
  cv.imwrite('images/xp-{}.jpg'.format(angle), res)

cv.destroyAllWindows()
