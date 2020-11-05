# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 23:56:37 2020

@author: user
"""

import cv2

# Haar Cascade 로 생성된 분류기 파일 읽기
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# 분석에 사용할 이미지를 gray scale 로 읽기
img = cv2.imread('000008.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# gray2 = cv2.equalizeHist(gray)

# 이미지에서 얼굴부분 인식
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for (x,y,w,h) in faces:

    # 얼굴의 위치를 사각형(or 원형)으로 표시 
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    # cv2.circle(img,(x+int(w*0.5),y+int(h*0.5)),int(0.5*h),(255,0,0),2) # circle(image, center, radius, color, thickness)

    # 얼굴 인식 영역 내부에서만 눈 인식함
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)

    # 눈이 검출된 회수만큼 눈 좌표 읽기
    for (ex,ey,ew,eh) in eyes:
        # 원본 이미지에 눈의 위치 표시
        # cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        cv2.circle(roi_color,(ex+int(ew*0.5),ey+int(eh*0.5)),int(0.5*eh),(255,0,0),2) # circle(imae, center, radius, color, thickness)
        
        eye_gray = gray[y+ey:y+ey+eh, x+ex:x+ex+ew]
        eye_color = img[y+ey:y+ey+eh, x+ex:x+ex+ew]
        _, threshold = cv2.threshold(eye_gray, 30, 255, cv2.THRESH_BINARY)
        cv2.imshow('img_gray',eye_gray)
        cv2.imshow('img_color',eye_color)
        cv2.imshow('img_threshold',threshold)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
       
        contours, _ = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        
        for contour in contours:
            ratio_area = cv2.contourArea(contour)/eh/ew
            # print(ratio_area)
            if ratio_area > 0.003 and ratio_area < 0.009:
                # print(ratio_area)
                # contour = cv2.convexHull(contour)
                xc, yc, wc, hc = cv2.boundingRect(contour)
                # cv2.rectangle(img,(x+ex+xc, y+ey+yc),(x+ex+xc+, y+ey+yc+hc), (0,255,0),2 )
                cv2.circle(eye_color,(xc+int(wc*0.5),yc+int(hc*0.5)),int(0.5*wc),(0,255,0),2)
                # cv2.imshow('img',img)
                # cv2.waitKey(0)
                # cv2.destroyAllWindows()       

# 얼굴 및 눈 인식 결과를 이미지에 표
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
