import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from collections import Counter


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

def main_info():
    print(f'Total columns in data = {len(get_columns())}')
    print(f'In 2010 in UK Constituencies = {constituencies}')

main_info()

def check_null():
    df = load_uk()
    return df[df['Election Year'].isnull()]

def load_uk_scrubbed():
    """ Load and filter UK data """ 
    df = load_uk()
    print(df[df['Election Year'].notnull()])

def count_columns(col_name: str):
    """ Number values of columns """
    return load_uk_scrubbed()[col_name].count()

print(count_columns('Electorate'))
