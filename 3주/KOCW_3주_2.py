# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 16:49:53 2020

AI보안 영상인식 3주차
@author: cspark@iscu.ac.kr
"""

import open3d as o3d
import numpy as np

print("Testing IO for meshes ...")
mesh = o3d.io.read_triangle_mesh("knot.ply")
print(mesh)
o3d.io.write_triangle_mesh("copy_of_knot.ply",mesh)
