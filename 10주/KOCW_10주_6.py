# -*- coding: utf-8 -*-
"""
7주차. OpenCV 기반 영상처리 1

@author: cspark@iscu.ac.kr
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

imgfile = 'wall-e-in-trashworld.jpg'
img = mpimg.imread(imgfile)

fig = plt.figure()
label = ['(a)', '(b)','(c)','(d)','(e)']

for i in range(1,5):
    ax = fig.add_subplot(2, 2, i)
    ax.imshow(img)
    ax.set_xlabel(label[i-1])
    ax.set_xticks([])
    ax.set_yticks([])
    
plt.show()

