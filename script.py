import pandas as pd
from pyclustering.samples.definitions import FCPS_SAMPLES
from pyclustering.utils import read_sample
from cluster import Cluster
from cure import Cure
from queue import Queue
import numpy as np

data = pd.DataFrame(read_sample(FCPS_SAMPLES.SAMPLE_LSUN), columns=['X', 'y'])

print('\nExploring head data')
print(data.head())
print('\n')

print('\nDatasets info')
data.info()
print('\n')
print(data.describe())
print('\n')

cure = Cure(data)
cure.clusters[0].logAttributes()