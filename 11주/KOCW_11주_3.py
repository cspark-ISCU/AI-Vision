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

th_red_low = np.array([0, 100, 100])
th_red_up = np.array([40, 255, 255])
mask_red_img1 = cv2.inRange(img_hsv, th_red_low, th_red_up)

th_red_low = np.array([150, 100, 100])
th_red_up = np.array([180, 255, 255])
mask_red_img2 = cv2.inRange(img_hsv, th_red_low, th_red_up)

mask_red_img3 = cv2.add(mask_red_img1, mask_red_img2)

img_red = cv2.bitwise_and(img, img, mask=mask_red_img3)

cv2.imshow("BGR",img)
cv2.imshow('MASK (RED)',img_red)

cv2.waitKey(0)
cv2.destroyAllWindows()
