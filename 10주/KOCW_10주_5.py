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

ax1 = fig.add_subplot(1, 2, 1)
ax1.imshow(img)
ax1.set_title('image1')
ax1.axis('off')

ax2 = fig.add_subplot(1, 2, 2)
ax2.imshow(img)
ax2.set_title('image2')
ax2.axis('off')

plt.show()

