# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 16:49:53 2020

AI보안 영상인식 3주차
@author: cspark@iscu.ac.kr
"""

import open3d as o3d
import numpy as np

print("Load a polygon volume and use it to crop the original point cloud")
vol = o3d.visualization.read_selection_polygon_volume("cropped.json")
pcd = o3d.io.read_point_cloud("cloud_bin_0.pcd")
chair = vol.crop_point_cloud(pcd)
o3d.visualization.draw_geometries([chair]
                                  # zoom=0.7,
                                  # front=[0.5439, -0.2333, -0.8060],
                                  # lookat=[2.4615, 2.1331, 1.338],
                                  # up=[-0.1781, -0.9708, 0.1608]
                                  )
