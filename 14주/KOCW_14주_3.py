# -*- coding: utf-8 -*-
"""
AI보안영상인식 14주차

author: cspark@iscu.ac.kr
Reference:
    https://github.com/gramman75/opencv/blob/master/doc/12.imageMorphological/imageMorphological.rst
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

dotImage = cv2.imread('dot_image.png')
holeImage = cv2.imread('hole_image.png')


# kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(7,7))
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
# kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))

erosion = cv2.erode(dotImage,kernel,iterations = 1)
dilation = cv2.dilate(holeImage,kernel,iterations = 1)

opening = cv2.morphologyEx(dotImage, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(holeImage, cv2.MORPH_CLOSE,kernel)

images =[dotImage, erosion, opening, holeImage, dilation, closing]
titles =['Dot Image','Erosion','Opening','Hole Image', 'Dilation','Closing']
for i in range(6):
    plt.figure(i+1),plt.imshow(images[i]),plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
