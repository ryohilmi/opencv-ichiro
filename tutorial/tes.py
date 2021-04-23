import cv2 as cv
import numpy as np

cap = cv.VideoCapture(1)

while True:
  _, frame = cap.read()

  hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

  lower = np.array([2,50,50])
  upper = np.array([12,255,255])

  mask = cv.inRange(hsv, lower, upper)

  res = cv.bitwise_and(frame, frame, mask= mask)

  cv.imshow('Frame', frame)
  cv.imshow('Mask', mask)
  cv.imshow('Result', res)

  if cv.waitKey(1) == ord('c'):
    break

cv.destroyAllWindows()