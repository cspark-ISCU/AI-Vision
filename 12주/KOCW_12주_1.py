# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 19:16:10 2020

@author: user
"""

import cv2

# 적절한 cascade xml file 선택
cascade_file = "haarcascade_frontalface_default.xml"

# 이미지 읽고 gray scale 로 변환
img = cv2.imread("football1.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# cascade classifier 읽고 얼굴 이미지 인식
cascade = cv2.CascadeClassifier(cascade_file)
face_list = cascade.detectMultiScale(img_gray, scaleFactor=1.14, minNeighbors=1)

# 인식한 얼굴에 사각형 표시
color = (255, 0, 0)
for face in face_list:
	x, y, w, h = face
	cv2.rectangle(img, (x, y), (x+w, y+h), color, thickness=2)

    
cv2.imshow('Face Detection', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
