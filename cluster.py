import numpy as np


class Cluster:
    def __init__(self, index, points):
        self.index = index
        self.points =points
        self.centroid = None
        self.repr_points=np.array([])
        self.closest = None
        self.closest_cluster_distance = None
        self.nbr_repr= 3

        self.UpdateCentroid()
        #self.Update_repr_points()
        

    def UpdateCentroid(self):
        self.centroid = np.mean(self.points,axis=0)

    def Update_repr_points(self):
        print('centroide :',self.centroid)
        farthest_point = self.getFarthestPoint(self.centroid)
        self.repr_points = np.append(self.repr_points, [farthest_point])
        while (self.nbr_repr > len(self.repr_points) and len(self.points) > len(self.repr_points)):
            moy=np.mean(self.repr_points,axis=0)
            promoted = self.getFarthestPoint(moy)
            self.repr_points = np.append(self.repr_points, promoted)
            self.repr_points =np.reshape(self.repr_points,(-1,2))
        print('repr points:',self.repr_points)    
            


           

    def getFarthestPoint(self, a):
        max_distance = 0
        returned_point = a
        for point in (self.points):
            if point not in self.repr_points:
                dist = self.euclidean_distance(a, point)
                if (dist > max_distance):
                  max_distance = dist 
                  returned_point = point
        return returned_point
        

    def euclidean_distance(self, A, B):
        return ((A - B)**2).sum()

  
    def logAttributes(self):
        """
        print('\nLogging attributes :\n')
        print('Index ', self.index)
        print('Points ', self.points)
        print('Centroid ', self.centroid)"""
        print('Reprentatives points ', self.Update_repr_points())
    """    print('Closest cluster index : ', self.closest.index)
        print('Closest cluster distance : ', self.closest_cluster_distance)
        print('\n----------\n')"""
        
          
    
