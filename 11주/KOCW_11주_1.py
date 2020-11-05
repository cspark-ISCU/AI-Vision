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

th_blue_low = np.array([95, 50, 70])
th_blue_up = np.array([135, 255, 255])

mask_blue_img = cv2.inRange(img_hsv, th_blue_low, th_blue_up)

img_blue = cv2.bitwise_and(img, img, mask=mask_blue_img)

cv2.imshow("BGR",img)
cv2.imshow('MASK (BLUE)',img_blue)

cv2.waitKey(0)
cv2.destroyAllWindows()
