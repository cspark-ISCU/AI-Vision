# -*- coding: utf-8 -*-
"""
AI보안영상인식 14주차

author: cspark@iscu.ac.kr
Reference:
    https://webnautes.tistory.com/1248
"""

import cv2
import numpy as np

cap = cv2.VideoCapture("vtest.avi")

# 옵션 설명 http://layer0.authentise.com/segment-background-using-computer-vision.html
fgbg = cv2.createBackgroundSubtractorMOG2(varThreshold=100)

while True:
    ret, frame = cap.read()
    if frame is None:
        break
    
    fgmask = fgbg.apply(frame)

    nlabels, labels, stats, centroids = cv2.connectedComponentsWithStats(fgmask)

    for index, centroid in enumerate(centroids):
        if stats[index][0] == 0 and stats[index][1] == 0:
            continue
        if np.any(np.isnan(centroid)):
            continue

        x, y, width, height, area = stats[index]
        centerX, centerY = int(centroid[0]), int(centroid[1])

        if area > 100:
            cv2.circle(frame, (centerX, centerY), 1, (0, 255, 0), 2)
            cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 0, 255))

    cv2.imshow('mask',fgmask)
    cv2.imshow('frame',frame)

    keyboard = cv2.waitKey(1) & 0xFF
    if keyboard == 27:
        break

cap.release()
cv2.destroyAllWindows()