import numpy as np


class Cluster:
    def __init__(self, index, points, repr_points=np.array([]), closest=None):
        self.index = index
        self.points = points
        self.centroid = None
        self.repr_points = points[0]
        self.closest = closest
        self.closest_cluster_distance = None

        self.UpdateCentroid()

    def UpdateCentroid(self):
        self.centroid = np.mean(self.points, axis=0)

    def logAttributes(self):
        print('\nLogging attributes :\n')
        print('Index ', self.index)
        print('Points ', self.points)
        print('Centroid ', self.centroid)
        print('Reprentatives points ', self.repr_points)
        print('Closest cluster index : ', self.closest.index)
        print('Closest cluster distance : ', self.closest_cluster_distance)
        print('\n----------\n')
