import pandas as pd
from pyclustering.samples.definitions import FCPS_SAMPLES
from pyclustering.utils import read_sample
from cluster import Cluster
from cure import Cure
from queue import Queue
import numpy as np

data = pd.DataFrame(read_sample(FCPS_SAMPLES.SAMPLE_LSUN), columns=['X', 'y'])

print('Exploring head data')
print(data.head())
print('\n\n')

print('Datasets info')
print(data.info())
print('\n')
print(data.describe())
print('\n\n')

a=np.array([2,3])
cure = Cure(data)
print('REPR : ')
cl= Cluster(
    5,
    np.array([
        [1, 2],
        [2, 3],
        [3, 4],
        [1, 4],
        [2, 3],
    ])
)

cl.Update_repr_points()

