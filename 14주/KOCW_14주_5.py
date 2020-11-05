# -*- coding: utf-8 -*-
"""
AI보안영상인식 14주차

author: cspark@iscu.ac.kr
Reference: https://docs.opencv.org/3.4.3/db/d5c/tutorial_py_bg_subtraction.html
"""

import cv2 as cv
import numpy as np

#### create Background Subtractor objects
backSub = cv.createBackgroundSubtractorMOG2()
# backSub = cv.bgsegm.createBackgroundSubtractorMOG()
# backSub = cv.bgsegm.createBackgroundSubtractorGMG()
# backSub = cv.createBackgroundSubtractorKNN()

## [capture]
capture = cv.VideoCapture('vtest.avi')
# capture = cv.VideoCapture('AD_street_parking_santafe_set1_no1_20200818.mp4')
# capture = cv.VideoCapture('43653691_20200211-14h19m22s_R_P.mp4')

kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5,5))
# kernel = np.ones((3,3), np.uint8)
while True:
    ret, frame = capture.read()
    if frame is None:
        break

    ## [apply]
    #update the background model
    fgMask = backSub.apply(frame)
    # fgMask_filter = cv.fastNlMeansDenoising(fgMask,3,21,7)
    # fgMask_blur = cv.GaussianBlur(fgMask, (5,5),0)
    fgMask_morph = cv.morphologyEx(fgMask, cv.MORPH_OPEN, kernel)
    # fgMask_morph = cv.morphologyEx(fgMask_morph, cv.MORPH_CLOSE, kernel)
    ## [apply]

    ## [display_frame_number]
    #get the frame number and write it on the current frame
    cv.rectangle(frame, (10, 2), (100,20), (255,255,255), -1)
    cv.putText(frame, str(capture.get(cv.CAP_PROP_POS_FRAMES)), (15, 15),
               cv.FONT_HERSHEY_SIMPLEX, 0.5 , (0,0,0))
    ## [display_frame_number]

    ## [show]
    #show the current frame and the fg masks
    cv.imshow('Frame', frame)
    cv.imshow('FG Mask', fgMask)
    # cv.imshow('FG Mask Filtered', fgMask_filter)
    # cv.imshow('FG Mask Blur', fgMask_blur)
    cv.imshow('FG Mask Blur', fgMask_morph)
    ## [show]

    keyboard = cv.waitKey(1) & 0xFF
    if keyboard == 27:
        break
capture.release()
cv.destroyAllWindows()
