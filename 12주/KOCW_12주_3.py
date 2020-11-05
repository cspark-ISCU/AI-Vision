# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 21:30:58 2020

@author: user
"""

import face_recognition as fr
import cv2

image = cv2.imread('football1.jpg')
face_locations = fr.face_locations(image, number_of_times_to_upsample=2)

for face_location in face_locations:

    # 이미지에서 얼굴이 인식된 위치를 기록
    top, right, bottom, left = face_location

    # 얼굴 위치에 사각형 추가
    cv2.rectangle(image,(left,top),(right,bottom),(255,0,0),2)

# 결과를 화면에 표시함
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
