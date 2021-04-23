import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while True:
  _, image = cap.read()

  hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

  lower_red = np.array([170, 100, 100])
  upper_red = np.array([180, 255, 255])
  red_mask = cv.inRange(hsv, lower_red, upper_red)

  lower_blue = np.array([100, 50, 50])
  upper_blue = np.array([120, 255, 255])
  blue_mask = cv.inRange(hsv, lower_blue, upper_blue)

  red_contour, red_hirearchy = cv.findContours(red_mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

  for i, contour in enumerate(red_contour):
    area = cv.contourArea(contour)
    if (area > 400):
      x, y, w, h = cv.boundingRect(contour)
      cv.rectangle(red_mask, (x, y), (x + w, y + h), (255, 255, 255), -1)

  blue_mask = cv.bitwise_and(blue_mask, red_mask)

  red_contour, _ = cv.findContours(red_mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
  blue_contour, _ = cv.findContours(blue_mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

  for i, contour in enumerate(red_contour):
    area = cv.contourArea(contour)
    if (area > 400):
      x, y, w, h = cv.boundingRect(contour)
      cv.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
      cv.putText(image, "Red color", (x, y), cv.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255))
    
  for i, contour in enumerate(blue_contour):
    area = cv.contourArea(contour)
    if (area > 400):
      x, y, w, h = cv.boundingRect(contour)
      cv.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
      cv.putText(image, "Blue color", (x, y), cv.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 0))  

  cv.imshow("Result", image)

  if cv.waitKey(1) == ord("c"):
    break

cv.destroyAllWindows()