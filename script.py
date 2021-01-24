import pandas as pd
from pyclustering.samples.definitions import FCPS_SAMPLES
from pyclustering.utils import read_sample
from cluster import Cluster
from cure import Cure

data = pd.DataFrame(read_sample(FCPS_SAMPLES.SAMPLE_LSUN), columns=['X', 'y'])

print('Exploring head data')
print(data.head())
print('\n\n')

print('Datasets info')
print(data.info())
print('\n')
print(data.describe())
print('\n\n')

cure = Cure(data)

print(cure.clusters[0].logAttributes())