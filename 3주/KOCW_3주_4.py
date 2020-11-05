# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 16:49:53 2020

AI보안 영상인식 3주차
@author: cspark@iscu.ac.kr
"""

import open3d as o3d
import numpy as np

pcd = o3d.io.read_point_cloud("cloud_bin_0.pcd")
print(pcd)
print(np.asarray(pcd.points))

o3d.visualization.draw_geometries([pcd],
                                  window_name='Test123',
                                  # width=10,
                                  # height=500,
                                  # left=100,
                                  # top=100,
                                  )