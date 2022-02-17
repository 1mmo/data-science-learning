import numpy as np
import pandas as pd
import scipy as sp
from matplotlib import pyplot as plt
from scipy import stats


def get_rvs():
    """ Show histogram of uniform distribution
        of synthetic dataset """
    xs = stats.uniform.rvs(0, 1, 10000)
    pd.Series(xs).hist(bins=20)
    plt.xlabel("Равномерное распределение")
    plt.ylabel("Частота")
    plt.show()

def bootstrap(xs, n, replace=True):
    """ Вернуть список массивов меньших размеров
        по n элементов каждый """
    return np.random.choice(xs, (len(xs), n), replace=replace)

def ex_1_16():
    xs = stats.uniform.rvs(loc=0, scale=1, size=10000)
    print(bootstrap(xs, 10))
    #plt.xlabel('Распределение средних значений')
    #plt.ylabel('Частота')
    #plt.show()

ex_1_16()
