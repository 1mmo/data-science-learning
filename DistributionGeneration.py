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

#ex_1_19()

def get_skew():
    s = dishonest_baker(950, 30)
    return {'mean': s.mean(),
            'median': s.median(),
            'asymmetry': s.skew() }

def qqplot(xs):
    """ Квантильный график (график квантиль-квантиль, Q-Q plot) """
    d = {0:sorted(stats.norm.rvs(loc=0, scale=1, size=len(xs))),
         1:sorted(xs)}
    pd.DataFrame(d).plot.scatter(0, 1, s=5, grid=True)
    plt.xlabel('Квантили теоретического нормального распределения')
    plt.ylabel('Квантили данных')
    plt.title('Квантильный график', fontweight='semibold')

def ex_1_21():
    '''Показать квантильные графики 
       для честного и нечестного булочников'''
    qqplot( honest_baker(1000, 30) )
    plt.show()
    qqplot( dishonest_baker(950, 30) )
    plt.show()

ex_1_21()
