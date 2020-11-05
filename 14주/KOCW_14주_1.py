# -*- coding: utf-8 -*-
"""
AI보안영상인식 14주차

author: cspark@iscu.ac.kr
Reference:
    https://opencv-python.readthedocs.io/en/latest/doc/11.imageSmoothing/imageSmoothing.html
"""

import cv2
from matplotlib import pyplot as plt

img = cv2.imread('lena.jpg')

# pyplot를 사용하기 위해서 BGR을 RGB로 변환함
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 일반 Blur
dst1 = cv2.blur(img,(5,5))

# GaussianBlur
dst2 = cv2.GaussianBlur(img,(5,5),0)

# Median Blur
dst3 = cv2.medianBlur(img,5)

# Bilateral Filtering
dst4 = cv2.bilateralFilter(img,9,75,75)

images = [img,dst1,dst2,dst3,dst4]
titles=['Original','Blur(7X7)','Gaussian Blur(5X5)','Median Blur','Bilateral']

for i in range(5):
    print(i)
    plt.figure(i+1),plt.imshow(images[i]),plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
