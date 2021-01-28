import pandas as pd
import matplotlib.pyplot as plt
from pyclustering.samples.definitions import FCPS_SAMPLES
from pyclustering.utils import read_sample
from cluster import Cluster
from cure import Cure
from queue import Queue
import numpy as np

if __name__ == '__main__':

    data = pd.DataFrame(read_sample(FCPS_SAMPLES.SAMPLE_LSUN),
                        columns=['X', 'y']).sample(100)

    print('\nExploring head data')
    print(data.head())
    print('\n')

    print('\nDatasets info')
    data.info()
    print('\n')
    print(data.describe())
    print('\n')

    cure = Cure(data)

    cure.visualizeData()

    cure.run()
    cure.write_labels()

    cure.visualizeClusters()

    # for cluster in cure.clusters:
    #     cluster.logAttributes()