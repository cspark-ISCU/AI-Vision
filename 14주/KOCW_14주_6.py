# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 17:17:21 2020

@author: user
@reference: https://dsbook.tistory.com/180
"""

import cv2
import numpy as np

capture = cv2.VideoCapture("vtest.avi")

histogram = None
# 검색 중지 요건
terminal = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 15, 0.5)

while capture.isOpened():
    ret, frame = capture.read()
    if not ret:
        break
    draw = frame.copy()
    
    if histogram is not None:
        # HSV space로 변환
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # 역투영
        dst = cv2.calcBackProject([hsv], [0], histogram, [0,180], 1)
        # 평균 이동 추적
        ret, (x,y,w,h) = cv2.meanShift(dst, (x,y,w,h), terminal)
        cv2.rectangle(draw,(x,y), (x+w, y+h), (0,255,0), 2)
        # 추적 영상 및 역투영 영상 동시 출력
        result = np.hstack((draw, cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)))
    else :
        cv2.putText(draw, "Target", (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 1, cv2.LINE_AA)
        result = draw
    
    cv2.imshow("MeanShift Tracking", result)
    key = cv2.waitKey(10) & 0xff
    if key == 27:
        break
    elif key == ord(' '):
        # space bar를 누른 후 ROI 설정
        x,y,w,h = cv2.selectROI("MeanShift Tracking", frame, False)
        # histogram 계산 및 정규화
        if w and h :
            roi = frame[y:y+h, x:x+w]
            roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
            histogram = cv2.calcHist([roi], [0], None, [180], [0,180])
            cv2.normalize(histogram, histogram, 0, 255, cv2.NORM_MINMAX)
        else:
            histogram = None

capture.release()
cv2.destroyAllWindows()
