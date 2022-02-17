import math
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from collections import Counter
from typing import List


def load_uk():
    """ The load UK data """
    return pd.read_excel('data/UK2010.xls')

def get_columns():
    """ Show all columns """
    return load_uk().columns

def check_columns(col_name: str) -> pd.Series:
    """ Get value of column """
    return load_uk()[col_name].unique()

def count_nan():
    """ Count unique values """
    return Counter(load_uk()['Election Year'])

constituencies = list(count_nan().values())[0]


def check_null():
    df = load_uk()
    return df['Electorate'].isnull()
print(check_null())

def load_uk_scrubbed():
    """ Load and filter UK data """ 
    df = load_uk()
    return df[df['Electorate'].notnull()]

def count_columns(col_name: str):
    """ Number values of columns """
    return load_uk_scrubbed()[col_name].count()

def median(xs: List[float]) -> float:
    n = len(xs)
    mid = n // 2
    if n % 2 == 0:
        return ((sorted(xs)[mid-1] + sorted(xs)[mid]) / 2)
    else:
        return sorted(xs)[mid]

def variance(xs: List[float]) -> float:
    mu = xs.mean()
    n = len(xs)
    n = n-1 if n in range(1, 30) else n
    square_deviation = lambda x: (x - mu) ** 2
    return sum(map(square_deviation, xs)) / n

def standard_deviation(xs: List[float]) -> float:
    return math.sqrt(variance(xs))

def get_quantile() -> pd.Series:
    q = [0, 1/4, 1/2, 3/4, 1]
    return load_uk_scrubbed()['Electorate'].quantile(q=q)

def nbin(n: int, xs: List[float]) -> List:
    """ Breakdown of data into frequency bins """
    min_x, max_x = min(xs), max(xs)
    range_x = max_x - min_x
    fn = lambda x: min(int((abs(x) - min_x) / range_x * n), n-1 )
    return map(fn, xs)

def point_bins():
    series = load_uk_scrubbed()['Electorate']
    return Counter(nbin(5, series))

print(point_bins())
   
def main_info():
    print('\n')
    print(f'Total columns in data = {len(get_columns())}')
    print(f'In 2010 in UK Constituencies = {constituencies}')
    mean_electorate = load_uk_scrubbed()['Electorate'].mean()
    print(f'Electorate mean values = {mean_electorate}')
    median_electorate = (load_uk_scrubbed()['Electorate']).median()
    print(f'Median of columns "Electorate" = {median_electorate}')
    variance_electorate = variance(load_uk_scrubbed()['Electorate'])
    print(f'Variance of columns "Electorate" = {variance_electorate}')
    standard_deviation_electorate = load_uk_scrubbed()['Electorate'].std(ddof=0)
    print(f'Standard deviation of columns "Electorate" = {standard_deviation_electorate}')
    print(f'Quantiles of columns "Electorate" \n {get_quantile()}')

main_info()

