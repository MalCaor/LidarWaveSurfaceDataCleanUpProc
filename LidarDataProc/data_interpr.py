# IMPORT EXTERN
from typing import List
import open3d as o3d

# IMPORT CLASS
from LidarPointArray import LidarPointArray

def shape_interpr(array_lidar: List[LidarPointArray]):
    length: float = len(array_lidar)
    print("Interpreting array of length {}".format(str(length)))
    list_mesh_retour: List[List[o3d.geometry.TriangleMesh]] = []
    list_pc_retour: List[o3d.geometry.PointCloud] = []
    i = 0.0
    for arr in array_lidar:
        # percent
        print(" "*20, end='\r')
        percent: float = i / length * 100.0
        print("{:.0f}/{} - {:.2f}%".format(i, length, percent), end='\r')
        i += 1
        
        # create point cloud
        pc = o3d.geometry.PointCloud()
        pc.points = o3d.utility.Vector3dVector(arr.points_array)
        pc.estimate_normals()
        pc.orient_normals_towards_camera_location()
        list_pc_retour.append(pc)
        # GeneMesh from Cloud
        list_mesh_retour.append(generate_mesh_from_inst_pc(pc))
    return (list_mesh_retour, list_pc_retour)

def generate_mesh_from_inst_pc(pc: o3d.geometry.PointCloud):
    list_retour: List[o3d.geometry.TriangleMesh] = []
    # gene mesh
    tetra_mesh, pt_map =  o3d.geometry.TetraMesh.create_from_point_cloud(pc)
    mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_alpha_shape(
        pc, 0.1, tetra_mesh, pt_map)
    list_retour.append(mesh)
    return list_retour