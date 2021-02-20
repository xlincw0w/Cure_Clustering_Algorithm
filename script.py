import pandas as pd
import matplotlib.pyplot as plt
from cluster import Cluster
from cure import Cure
from queue import Queue
import numpy as np

if __name__ == '__main__':

    data = pd.read_csv('./data/sample_data.csv')
    # data = pd.read_csv('./data/etudiant.csv')

    print('\nExploring head data')
    print(data.head())
    print('\n')

    print('\nDatasets info')
    data.info()
    print('\n')
    print(data.describe())
    print('\n')

    cure = Cure(data, cluster_nbr=3, nbr_repr=4)

    cure.visualizeData()
    cure.run()

    input('Press any key !')
    cure.visualizeClusters()