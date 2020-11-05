# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 11:34:36 2020

@author: user
"""

import cv2
import face_recognition as fr
import numpy as np

# 이미지 읽고 얼굴 부위별 위치 인식하기
img = cv2.imread('000011.jpg')
face_locations = fr.face_locations(img, number_of_times_to_upsample=2)

for face_location in face_locations:

    # 이미지에서 얼굴이 인식된 위치를 기록
    top, right, bottom, left = face_location
    
    face_landmarks_list = fr.face_landmarks(img)
    
    pts = np.array(face_landmarks_list[0]['chin'])
    cv2.polylines(img, [pts], True, (255, 0, 0), 2)

    pts = np.array(face_landmarks_list[0]['left_eyebrow'])
    cv2.polylines(img, [pts], True, (0, 255, 0), 2)

    pts = np.array(face_landmarks_list[0]['right_eyebrow'])
    cv2.polylines(img, [pts], True, (0, 255, 0), 2)

    pts = np.array(face_landmarks_list[0]['left_eye'])
    cv2.polylines(img, [pts], True, (0, 255, 0), 2)

    pts = np.array(face_landmarks_list[0]['right_eye'])
    cv2.polylines(img, [pts], True, (0, 255, 0), 2)

    pts = np.array(face_landmarks_list[0]['nose_bridge'])
    cv2.polylines(img, [pts], True, (0, 255, 0), 2)

    pts = np.array(face_landmarks_list[0]['nose_tip'])
    cv2.polylines(img, [pts], True, (0, 255, 0), 2)

    pts = np.array(face_landmarks_list[0]['top_lip'])
    cv2.polylines(img, [pts], True, (0, 255, 0), 2)

    pts = np.array(face_landmarks_list[0]['bottom_lip'])
    cv2.polylines(img, [pts], True, (0, 255, 0), 2)

    # 얼굴 위치에 사각형 추가
    cv2.rectangle(img,(left,top),(right,bottom),(255,0,0),2)


    # 결과를 화면에 표시함
    cv2.imshow('Image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

