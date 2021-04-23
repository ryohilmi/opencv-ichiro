import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while True:
  _, frame = cap.read()

  hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

  lower_orange = np.array([3,50,50])
  upper_orange = np.array([12,255,255])

  lower_yellow = np.array([18, 50, 50])
  upper_yellow = np.array([28, 255, 255])

  orange_mask = cv.inRange(hsv, lower_orange, upper_orange)
  yellow_mask = cv.inRange(hsv, lower_yellow, upper_yellow)

  final_mask = orange_mask + yellow_mask

  res = cv.bitwise_and(frame, frame, mask= final_mask)

  cv.imshow('Frame', frame)
  cv.imshow('Mask', final_mask)
  cv.imshow('Result', res)

  k = cv.waitKey(1)
  if k == ord('c'):
    break

cv.destroyAllWindows()