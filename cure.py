import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from cluster import Cluster
from queue import Queue
from threading import Thread
from multiprocessing import Process
from time import time


class Cure:
    def __init__(self, data, cluster_nbr=3, nbr_repr=4, compression=0.5):
        self.data = data
        self.cluster_nbr = cluster_nbr
        self.nbr_repr = nbr_repr
        self.compression = compression
        self.clusters = np.array([])

        self.result = self.data

        self.initClusters()
        self.initClosestCluster(0, len(self.clusters), '#')

        # Clusters queue
        self.q = Queue(arr=self.clusters)

    def initClusters(self):
        for row in self.data.iterrows():
            index = row[0]
            x_val = row[1]['X']
            y_val = row[1]['y']

            self.clusters = np.append(
                self.clusters,
                Cluster(index, np.array([[x_val, y_val]], dtype='float16'),
                        self.nbr_repr))

    def initClosestCluster(self, start, end, thread_id):
        for i in range(start, end):
            closest = None
            distance = 99999
            for clus in self.clusters:
                min_clus_dist = self.min_cluster_distance(
                    self.clusters[i], clus)
                if (min_clus_dist < distance):
                    closest = clus
                    distance = min_clus_dist

            self.clusters[i].closest = closest
            self.clusters[i].closest_cluster_distance = distance

    # def UpdateClosestCluster(self, cluster):
    #     closest = None
    #     distance = 99999
    #     for clus in self.clusters:
    #         min_clus_dist = self.min_cluster_distance(cluster, clus)
    #         if (min_clus_dist < distance):
    #             closest = clus
    #             distance = min_clus_dist

    #     cluster.closest = closest
    #     cluster.closest_cluster_distance = distance

    def min_cluster_distance(self, cluster_a, cluster_b):
        distance = 99999
        for point_a in cluster_a.repr_points:
            for point_b in cluster_b.repr_points:
                calc_dist = self.euclidean_distance(point_a, point_b)
                if (cluster_a.index != cluster_b.index
                        and calc_dist < distance):
                    distance = calc_dist

        return distance

    def run(self):
        before = time()
        while (len(self.clusters) > self.cluster_nbr):
            cl = self.q.dequeue()
            closest = cl.closest

            index = cl.index
            new_points = np.concatenate((cl.points, closest.points), axis=0)
            nbr_repr = self.nbr_repr

            i = 0
            max_length = len(self.clusters)

            cluster_to_kick = np.array([], dtype='int8')

            for i in range(0, len(self.clusters)):
                if (self.clusters[i].index == index
                        or self.clusters[i].index == closest.index):
                    cluster_to_kick = np.append(cluster_to_kick, i)

            self.clusters = [
                self.clusters[i] for i in range(0, len(self.clusters))
                if i not in cluster_to_kick
            ]

            new_cluster = Cluster(index=index,
                                  points=new_points,
                                  nbr_repr=nbr_repr)

            self.q = Queue(arr=self.clusters)
            self.clusters = np.append(self.clusters, new_cluster)

            self.initClosestCluster(0, len(self.clusters), '0')

            # Threads = []
            # nbr_threads = 10
            # track = int(len(self.clusters) / nbr_threads)
            # diff = len(self.clusters) - track * nbr_threads

            # for i in range(0, nbr_threads):
            #     added_value = 0

            #     if (i == nbr_threads - 1):
            #         added_value = diff

            #     Threads = np.append(
            #         Threads,
            #         Process(target=self.initClosestCluster,
            #                 args=(
            #                     track * i,
            #                     track * (i + 1) + added_value,
            #                     i,
            #                 )))

            # for th in Threads:
            #     th.start()

            # for th in Threads:
            #     th.join()

            # track = int(len(self.clusters) / 5)
            # diff = len(self.clusters) - track * 5

            # Th1 = Thread(target=self.initClosestCluster,
            #              args=(
            #                  0,
            #                  track,
            #                  '1',
            #              ))
            # Th2 = Thread(target=self.initClosestCluster,
            #              args=(track, track * 2, '2'))
            # Th3 = Thread(target=self.initClosestCluster,
            #              args=(track * 2, track * 3, '3'))
            # Th4 = Thread(target=self.initClosestCluster,
            #              args=(
            #                  track * 3,
            #                  track * 4,
            #                  '4',
            #              ))
            # Th5 = Thread(target=self.initClosestCluster,
            #              args=(
            #                  track * 4,
            #                  track * 5 + diff,
            #                  '5',
            #              ))

            # Th1.start()
            # Th2.start()
            # Th3.start()
            # Th4.start()
            # Th5.start()

            # Th1.join()
            # Th2.join()
            # Th3.join()
            # Th4.join()
            # Th5.join()

            self.q = Queue(arr=self.clusters)
            self.q.enqueue(new_cluster)

        for i in range(0, len(self.clusters)):
            self.clusters[i].index = i

        print('Time consumed : ', int(time() - before), 'sec')

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

    def write_labels(self):
        clus1 = pd.DataFrame(self.clusters[0].points, columns=['X', 'y'])
        clus1['Cluster'] = 0
        clus2 = pd.DataFrame(self.clusters[1].points, columns=['X', 'y'])
        clus2['Cluster'] = 1
        clus3 = pd.DataFrame(self.clusters[2].points, columns=['X', 'y'])
        clus3['Cluster'] = 2

        result = pd.concat([clus1, clus2, clus3])
        self.result = result

    def visualizeData(self):
        plt.figure(figsize=(14, 8))
        plt.scatter(
            self.data['X'],
            self.data['y'],
        )
        plt.show()

    def visualizeClusters(self):
        plt.figure(figsize=(14, 8))
        plt.scatter(self.result['X'],
                    self.result['y'],
                    c=self.result['Cluster'])
        plt.show()
