from typing import List
from LidarPoint import LidarPoint
from LidarPointArray import LidarPointArray
import pandas as pd

from matplotlib import pyplot as plt
from matplotlib import animation as anim
import seaborn

def display2DcloudPoint(array_cloud: List[LidarPoint]):
    points = []
    for point in array_cloud:
        points.append({
            "longitude" : point.x,
            "latitude" : point.y
        })
    data = pd.DataFrame(points)
    seaborn.jointplot(x="longitude", y="latitude", data=data, s=0.5)
    plt.show()

def hex2dcloudPoint(array_cloud: List[LidarPoint]):
    x = []
    y = []
    z = []
    for point in array_cloud:
        x.append(point.x)
        y.append(point.y)
        z.append(point.z)
    plt.hexbin(x, y, C=z)
    plt.xlabel('x coordinates')
    plt.ylabel('y coordinates')
    plt.show()

def contour2dcloudPoint(array_cloud: List[LidarPoint]):
    x = []
    y = []
    z = []
    for point in array_cloud:
        x.append(point.x)
        y.append(point.y)
        z.append(point.z)
    plt.tricontourf(x, y, z, cmap="ocean")
    plt.xlabel('x coordinates')
    plt.ylabel('y coordinates')
    plt.show()

def contour2dAnimates(array_cloud: List[LidarPointArray]):
    print("join plot")
    plt.tricontourf(
        [p[0] for p in array_cloud[0].points_array],
        [p[1] for p in array_cloud[0].points_array],
        [p[2] for p in array_cloud[0].points_array]
    )
    print("display plot")
    plt.show()