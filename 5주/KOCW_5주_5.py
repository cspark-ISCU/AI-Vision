# Open3D: www.open3d.org
# The MIT License (MIT)
# See license file or visit www.open3d.org for details

# reference: http://www.open3d.org/docs/release/tutorial/Advanced/color_map_optimization.html

import open3d as o3d
import re
import os
# import open3d_tutorial as o3dtut

# if running on Travis CI, the number of iterations is reduced
is_ci = "CI" in os.environ

def sorted_alphanum(file_list_ordered):
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(file_list_ordered, key=alphanum_key)

def get_file_list(path, extension=None):
    if extension is None:
        file_list = [path + f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    else:
        file_list = [
            path + f
            for f in os.listdir(path)
            if os.path.isfile(os.path.join(path, f)) and os.path.splitext(f)[1] == extension
        ]
    file_list = sorted_alphanum(file_list)
    return file_list

# path = o3dtut.download_fountain_dataset()
debug_mode = False

rgbd_images = []
depth_image_path = get_file_list("depth/", extension=".png")
color_image_path = get_file_list("image/", extension=".jpg")
assert (len(depth_image_path) == len(color_image_path))
for i in range(len(depth_image_path)):
    depth = o3d.io.read_image(os.path.join(depth_image_path[i]))
    color = o3d.io.read_image(os.path.join(color_image_path[i]))
    rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(
        color, depth, convert_rgb_to_intensity=False)
    if debug_mode:
        pcd = o3d.geometry.PointCloud.create_from_rgbd_image(
            rgbd_image,
            o3d.camera.PinholeCameraIntrinsic(
                o3d.camera.PinholeCameraIntrinsicParameters.
                PrimeSenseDefault))
        o3d.visualization.draw_geometries([pcd])
    rgbd_images.append(rgbd_image)


camera = o3d.io.read_pinhole_camera_trajectory("scene/key.log")
mesh = o3d.io.read_triangle_mesh("scene/integrated.ply")

# Before full optimization, let's just visualize texture map
# with given geometry, RGBD images, and camera poses.
option = o3d.color_map.ColorMapOptimizationOption()
option.maximum_iteration = 0
with o3d.utility.VerbosityContextManager(o3d.utility.VerbosityLevel.Debug) as cm:
    o3d.color_map.color_map_optimization(mesh, rgbd_images, camera, option)
    
o3d.visualization.draw_geometries([mesh],
                                  # zoom=0.5399,
                                  # front=[0.0665, -0.1107, -0.9916],
                                  # lookat=[0.7353, 0.6537, 1.0521],
                                  # up=[0.0136, -0.9936, 0.1118]
                                  )


option.maximum_iteration = 100 if is_ci else 300
option.non_rigid_camera_coordinate = False ## False if Rigid Optimization
with o3d.utility.VerbosityContextManager(o3d.utility.VerbosityLevel.Debug) as cm:
    o3d.color_map.color_map_optimization(mesh, rgbd_images, camera, option)
    
o3d.visualization.draw_geometries([mesh]
                                  # , zoom=0.5399,
                                  # front=[0.0665, -0.1107, -0.9916],
                                  # lookat=[0.7353, 0.6537, 1.0521],
                                  # up=[0.0136, -0.9936, 0.1118]
                                  )

