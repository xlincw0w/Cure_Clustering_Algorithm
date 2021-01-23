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


class Cluster:
    def __init__(self, index, points, centroid=0, repr_points=[]):
        self.index = index
        self.points = points
        self.centroid = centroid
        self.repr_points = repr_points


class CureCluster:
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


Cure = CureCluster(data)
Cure.logAttributes()