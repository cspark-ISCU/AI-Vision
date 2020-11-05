# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 16:49:53 2020

AI보안 영상인식 4주차
@author: cspark@iscu.ac.kr
"""

import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt


pcd = o3d.io.read_point_cloud("fragment.ply")
plane_model, inliers = pcd.segment_plane(distance_threshold=0.015,
                                         ransac_n=3,
                                         num_iterations=1000)
[a, b, c, d] = plane_model
print(f"Plane equation: {a:.2f}x + {b:.2f}y + {c:.2f}z + {d:.2f} = 0")

inlier_cloud = pcd.select_by_index(inliers)
inlier_cloud.paint_uniform_color([1.0, 0, 0])
outlier_cloud = pcd.select_by_index(inliers, invert=True)

plane_model2, inliers2 = outlier_cloud.segment_plane(distance_threshold=0.025,
                                         ransac_n=3,
                                         num_iterations=1000)

inlier_cloud2 = outlier_cloud.select_by_index(inliers2)
inlier_cloud2.paint_uniform_color([0, 1.0, 0])
outlier_cloud2 = outlier_cloud.select_by_index(inliers2, invert=True)

# o3d.visualization.draw_geometries([inlier_cloud, inlier_cloud2, outlier_cloud])

with o3d.utility.VerbosityContextManager(o3d.utility.VerbosityLevel.Debug) as cm:  
    labels = np.array(outlier_cloud2.cluster_dbscan(eps=0.02, min_points=10, print_progress=True))

max_label = labels.max()
print(f"point cloud has {max_label + 1} clusters")
colors = plt.get_cmap("tab20")(labels / (max_label if max_label > 0 else 1))
colors[labels < 0] = 0
outlier_cloud2.colors = o3d.utility.Vector3dVector(colors[:, :3])


# o3d.visualization.draw_geometries([inlier_cloud, inlier_cloud2])
# o3d.visualization.draw_geometries([outlier_cloud2])
o3d.visualization.draw_geometries([inlier_cloud, inlier_cloud2, outlier_cloud2]
                                  # , zoom=0.455,
                                  # front=[-0.4999, -0.1659, -0.8499],
                                  # lookat=[2.1813, 2.0619, 2.0999],
                                  # up=[0.1204, -0.9852, 0.1215]
                                  )