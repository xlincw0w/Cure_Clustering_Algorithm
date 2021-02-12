import numpy as np


class Cluster:
    def __init__(self, index, points, nbr_repr, compression):
        self.index = index
        self.points = points
        self.centroid = None
        self.repr_points = np.array([])
        self.closest = None
        self.closest_cluster_distance = None
        self.nbr_repr = nbr_repr
        self.compression = compression
        self.UpdateCentroid()
        self.Update_repr_points()

    def UpdateCentroid(self):
        self.centroid = np.mean(self.points, axis=0)

    def Update_repr_points(self):
        queue_points = np.array([])
        queue_points = self.points
        farthest_point = self.getFarthestPoint(self.centroid, queue_points)
        self.repr_points = np.append(self.repr_points, [farthest_point])
        self.repr_points = np.reshape(self.repr_points, (-1, 2))
        queue_points = self.depop_array(queue_points)

        while (self.nbr_repr > (len(self.repr_points))
               and len(self.points) > len(self.repr_points)
               and len(queue_points) > 0):
            moy = np.mean(self.repr_points, axis=0)
            promoted = self.getFarthestPoint(moy, queue_points)
            self.repr_points = np.append(self.repr_points, promoted)
            self.repr_points = np.reshape(self.repr_points, (-1, 2))
            queue_points = self.depop_array(queue_points)
        self.repr_points = self.shrinking_repr()
        return self.repr_points

    def depop_array(self, arr):
        for i in self.repr_points:
            if i in arr and len(arr) > 0:
                index = np.where((i == arr[:, None]).all(-1))[0]
                arr = np.delete(arr, index, axis=0)
        return (arr)

    def getFarthestPoint(self, a, arr):
        max_distance = 0
        returned_point = a
        q_points = np.array([])
        q_points = arr
        for point in (q_points):
            dist = self.euclidean_distance(a, point)
            if (dist > max_distance):
                max_distance = dist
                returned_point = point
        return returned_point

    def cluster_size(self):
        return self.points.size

    def euclidean_distance(self, A, B):
        return ((A - B)**2).sum()

    def shrinking_repr(self):
        dist_centr = np.array([])
        for i in self.repr_points:
            dist_centr = np.append(
                dist_centr, i - (self.compression * (i - self.centroid)))
            dist_centr = np.reshape(dist_centr, (-1, 2))
        return (dist_centr)

    def logAttributes(self):
        print('\nLogging attributes :\n')
        print('Index ', self.index)
        print('Points ', self.points)
        print('Centroid ', self.centroid)
        print('Reprentatives points ', self.repr_points)
        print('Closest cluster index : ', self.closest.index)
        print('Closest cluster distance : ', self.closest_cluster_distance)
        print('\n----------\n')
