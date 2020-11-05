# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
import numpy as np

img = cv2.imread('2c_original.jpg')

# BGR 을 HSV 로 변경
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

th_green_low = np.array([50, 100, 100])
th_green_up = np.array([90, 255, 255])

mask_green_img = cv2.inRange(img_hsv, th_green_low, th_green_up)

img_green = cv2.bitwise_and(img, img, mask=mask_green_img)

cv2.imshow("BGR",img)
cv2.imshow('MASK (GREEN)',img_green)

cv2.waitKey(0)
cv2.destroyAllWindows()
