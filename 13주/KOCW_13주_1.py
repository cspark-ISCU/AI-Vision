# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 21:15:21 2020

@author: user
"""

import cv2 

# 얼굴과 눈을 인식하기 위한 xml 파일을 읽음
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# 이미지를 읽고 gray scale 로 변경
img = cv2.imread('000017.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 이미지에서 얼굴 인식
faces = face_cascade.detectMultiScale(gray, 1.14, 1)

# 검출된 얼굴 개수만큼 for 루프 동작
for (x,y,w,h) in faces:

    # 원본 이미지의 얼굴 위치에 사각형 그리기
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    # 눈 위치 인식은 검출된 얼굴 영역 내부에서만 진행
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]

    # 눈 위치 인식
    eyes = eye_cascade.detectMultiScale(roi_gray,1.31,3) 

    # 검출된 눈 개수만큼 for 루프 동작
    for (ex,ey,ew,eh) in eyes: 

        # 원본 이미지에 사각형으로 눈 위치 표시
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

# 결과를 화면에 표시함
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
