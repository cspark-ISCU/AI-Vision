# -*- coding: utf-8 -*-
"""
7주차. OpenCV 기반 영상처리 1

@author: cspark@iscu.ac.kr
"""

import cv2
import matplotlib.pyplot as plt

imgfile = 'wall-e-in-trashworld.jpg'
img = cv2.imread(imgfile, cv2.IMREAD_COLOR)

plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.title('Wall-E')
plt.axis('off')
plt.show()

