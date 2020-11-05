

import numpy as np
import open3d as o3d

source = o3d.io.read_point_cloud("fragment_000.ply")
o3d.visualization.draw_geometries([source])

source = o3d.io.read_point_cloud("fragment_001.ply")
o3d.visualization.draw_geometries([source])

source = o3d.io.read_point_cloud("fragment_002.ply")
o3d.visualization.draw_geometries([source])

source = o3d.io.read_point_cloud("fragment_003.ply")
o3d.visualization.draw_geometries([source])

source = o3d.io.read_point_cloud("fragment_004.ply")
o3d.visualization.draw_geometries([source])

source = o3d.io.read_point_cloud("fragment_005.ply")
o3d.visualization.draw_geometries([source])

source = o3d.io.read_point_cloud("fragment_006.ply")
o3d.visualization.draw_geometries([source])

source = o3d.io.read_point_cloud("fragment_007.ply")
o3d.visualization.draw_geometries([source])
