# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 15:09:08 2020

@author: user
"""


import cv2
from matplotlib import pyplot as plt

# img = cv2.imread('lena_noisy.png')
# dst = cv2.fastNlMeansDenoising(img,h=15)

img = cv2.imread('landscape_noisy.jpg')
dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)

plt.figure(1),plt.imshow(img)
plt.figure(2),plt.imshow(dst)
plt.show()