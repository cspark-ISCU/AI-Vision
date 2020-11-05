# -*- coding: utf-8 -*-
"""
AI보안영상인식 14주차

author: cspark@iscu.ac.kr
Reference: https://opencv-python.readthedocs.io/en/latest/doc/07.imageArithmetic/imageArithmetic.html
"""

import cv2 as cv

## [capture]
capture = cv.VideoCapture('vtest.avi')
# capture = cv.VideoCapture('AD_street_parking_santafe_set1_no1_20200818.mp4')
# capture = cv.VideoCapture('43653691_20200211-14h19m22s_R_P.mp4')

frame_index = 1
_, frame_prev = capture.read()
while True:
    frame_index = frame_index + 1
    _, frame = capture.read()
    if frame is None:
        break

    # beta = 98
    # frame_prev = cv.addWeighted(frame_prev, float(beta)/100, frame, float(100-beta)/100, 0)
    frame_prev = cv.addWeighted(frame_prev, (frame_index-1)/frame_index, frame, 1/frame_index, 0)

    ## [display_frame_number]
    #get the frame number and write it on the current frame
    cv.rectangle(frame, (10, 2), (100,20), (255,255,255), -1)
    cv.putText(frame, str(capture.get(cv.CAP_PROP_POS_FRAMES)), (15, 15),
                cv.FONT_HERSHEY_SIMPLEX, 0.5 , (0,0,0))
 
    ## [show]
    cv.imshow('Frame', frame)
    cv.imshow('Background', frame_prev)

    keyboard = cv.waitKey(1) & 0xFF
    if keyboard == 27:
        break
    
capture.release()
cv.destroyAllWindows()
