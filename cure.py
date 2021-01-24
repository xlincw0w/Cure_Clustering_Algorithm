import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pyclustering.samples.definitions import FCPS_SAMPLES
from pyclustering.utils import read_sample

data = pd.DataFrame(read_sample(FCPS_SAMPLES.SAMPLE_LSUN), columns=['X', 'y'])

print('Exploring head data')
print(data.head())
print('\n\n')

print('Datasets info')
print(data.info())
print('\n')
print(data.describe())
print('\n\n')


def euclidean_distance(A, B):
    return ((A - B)**2).sum()


def min_cluster_distance(cluster_a, cluster_b):
    distance = 99999
    for point_a in cluster_a.repr_points:
        for point_b in cluster_b.repr_points:
            calc_dist = euclidean_distance(point_a, point_b)
            if (cluster_a.index != cluster_b.index and calc_dist < distance):
                distance = calc_dist

    return distance


class Cluster:
    def __init__(self,
                 index,
                 points,
                 centroid=0,
                 repr_points=[],
                 closest=None):
        self.index = index
        self.points = points
        self.centroid = centroid
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


class Cure:
    def __init__(self, data, cluster_nbr=3, represent_nbr=4, compression=0.5):
        self.data = data
        self.cluster_nbr = cluster_nbr
        self.represent_nbr = represent_nbr
        self.compression = compression
        self.clusters = np.array([])

        self.initClusters()

    def initClusters(self):
        for row in self.data.iterrows():
            index = row[0]
            x_val = row[1]['X']
            y_val = row[1]['y']

            self.clusters = np.append(
                self.clusters, Cluster(index, np.array([[x_val, y_val]])))

    def initClosestCluster(self):
        for clus_1 in self.clusters:
            closest = None
            distance = 99999
            for clus_2 in self.clusters:
                min_clus_dist = min_cluster_distance(clus_1, clus_2)
                if (min_clus_dist < distance):
                    closest = clus_2
                    distance = min_clus_dist

            clus_1.closest = closest
            clus_1.closest_cluster_distance = distance

    def logAttributes(self):
        print('\nLogging attributes :\n')
        print('Data ', self.data)
        print('Clusters number ', self.cluster_nbr)
        print('Representatives points number', self.represent_nbr)
        print('Compression ', self.compression)
        print('Clusters : ', len(self.clusters))
        print('\n----------\n')

    def visualize(self):
        plt.scatter(self.data[0], self.data[1])
        plt.show()

    # def euclidean_distance(self)


cure = Cure(data)
cure.initClosestCluster()

print(cure.clusters[0].logAttributes())
