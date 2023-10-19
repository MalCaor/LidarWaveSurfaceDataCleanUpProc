from typing import List
import open3d as o3d
import numpy as np
from LidarPoint import LidarPoint

def display_point_cloud(array_cloud: List[LidarPoint]):
    print("Visualise Array of {} points".format(str(len(array_cloud))))
    
    vis = o3d.visualization.Visualizer()
    vis.create_window()

    geometry = o3d.geometry.PointCloud()
    # *optionally* add initial points
    points = np.random.rand(10, 3)
    geometry.points = o3d.utility.Vector3dVector(points)

    vis.add_geometry(geometry)
    
    for point in array_cloud:
        geometry.points.append(point.point3d())
        vis.update_geometry(geometry)
        vis.poll_events()
        vis.update_renderer()

    print("Finised")