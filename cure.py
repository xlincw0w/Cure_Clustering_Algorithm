import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from cluster import Cluster


class Cure:
    def __init__(self, data, cluster_nbr=3, represent_nbr=4, compression=0.5):
        self.data = data
        self.cluster_nbr = cluster_nbr
        self.represent_nbr = represent_nbr
        self.compression = compression
        self.clusters = np.array([])

        self.initClusters()
        self.initClosestCluster()

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
                min_clus_dist = self.min_cluster_distance(clus_1, clus_2)
                if (min_clus_dist < distance):
                    closest = clus_2
                    distance = min_clus_dist

            clus_1.closest = closest
            clus_1.closest_cluster_distance = distance

    def min_cluster_distance(self, cluster_a, cluster_b):
        distance = 99999
        for point_a in cluster_a.repr_points:
            for point_b in cluster_b.repr_points:
                calc_dist = self.euclidean_distance(point_a, point_b)
                if (cluster_a.index != cluster_b.index
                        and calc_dist < distance):
                    distance = calc_dist

        return distance

    def logAttributes(self):
        print('\nLogging attributes :\n')
        print('Data ', self.data)
        print('Clusters number ', self.cluster_nbr)
        print('Representatives points number', self.represent_nbr)
        print('Compression ', self.compression)
        print('Clusters : ', len(self.clusters))
        print('\n----------\n')

    def euclidean_distance(self, A, B):
        return ((A - B)**2).sum()

    def visualize(self):
        plt.scatter(self.data['X'], self.data['y'])
        plt.show()
