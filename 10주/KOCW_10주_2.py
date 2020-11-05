# -*- coding: utf-8 -*-
"""
7주차. OpenCV 기반 영상처리 1

@author: cspark@iscu.ac.kr
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

imgfile = 'wall-e-in-trashworld.jpg'
img = mpimg.imread(imgfile)

plt.imshow(img)
plt.title('Wall-E')
plt.xticks([])
plt.yticks([])
plt.show()

