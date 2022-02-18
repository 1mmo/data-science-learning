import pandas as pd
from scipy import stats 
from matplotlib import pyplot as plt

from RVS import bootstrap

def honest_baker(loc, scale):
    """
    Honest baker model 
    loc - mean value
    scale - variance
    size - sample size

    """
    return pd.Series(stats.norm.rvs(loc, scale, size=10000))

def honest_hist():
    """ Honest baker on histogram """
    honest_baker(1000, 30).hist(bins=25)
    plt.xlabel('Honest baker')
    plt.ylabel('Frequency')
    plt.show()

#honest_hist()

def dishonest_baker(loc, scale):
    """ Dishonest baker model """
    xs = stats.norm.rvs(loc, scale, size=10000)
    return pd.Series(map(max, bootstrap(xs, 13)))

def ex_1_19():
    '''Смоделировать нечестного булочника на гистограмме'''
    dishonest_baker(950, 30).hist(bins=25)
    plt.xlabel('Нечестный булочник') 
    plt.ylabel('Частота')
    plt.show()

dishonest_baker(950, 30)

def get_skew():
    s = dishonest_baker(950, 30)
    return {'mean': s.mean(),
            'median': s.median(),
            'asymmetry': s.skew() }

print(get_skew())
