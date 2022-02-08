import math
import matplotlib.pyplot as plt
from collections import Counter
from typing import List
from Vectors import sum_of_squares, dot


# Число друзей
num_friends = [100, 49, 41, 40, 25]
daily_hours = [5, 4, 3, 2, 1]

friend_counts = Counter(num_friends)
xs = range(101)
ys = [friend_counts[x] for x in xs]

plt.bar(xs, ys)
plt.axis([0, 101, 0, 25])
plt.title("Гистограмма количеств друзей")
plt.xlabel('Число друзей')
plt.ylabel('Число людей')
#plt.show()

num_points = len(num_friends)
largest_value = max(num_friends)
smallest_value = min(num_friends)

sorted_values = sorted(num_friends)
smallest_value = sorted_values[0]
second_smallest_value = sorted_values[1]
second_largest_value = sorted_values[-2]

# Среднее значение
def mean(xs: List[float]) -> float:
    return sum(xs) / len(xs)

def _median_odd(xs: List[float]) -> float:
    """ Если len(xs) является нечетной,
        то медиана - это средний элемент 
    """
    return sorted(xs)[len(xs) // 2]

def _median_even(xs: List[float]) -> float:
    """ Если len(xs) является четной, то она является средним значением
        двух срединных элементов 
    """
    sorted_xs = sorted(xs)
    hi_midpoint = len(xs) // 2 
    return (sorted_xs[hi_midpoint - 1] + sorted_xs[hi_midpoint] / 2)

def median(v: List[float]) -> float:
    """ Отыскивает 'ближайшнее к середине' значение v"""
    return _median_even(v) if len(v) % 2 == 0 else _median_odd(v)

def quantile(xs: List[float], p: float) -> float:
    """ Возвращает значение p-го процентиля в x """
    p_index = int(p * len(xs))
    return sorted(xs)[p_index]


def mode(x: List[float]) -> float:
    """ Возвращает список, т. к. может быть более одной моды """
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items()
            if count == max_count]

def data_range(xs: List[float]) -> float:
    return max(xs) - min(xs)

assert data_range(num_friends) == 75

def de_mean(xs: List[float]) -> List[float]:
    """ Транслировать xs путем вычитания его среднего """
    x_bar = mean(xs)
    return [x - x_bar for x in xs]

def variance(xs: List[float]) -> float:
    """ Почти среднеквадратическое отклонение от среднего """
    assert len(xs) >= 2, 'дисперсия требует наличия не менее двух элементов'

    n = len(xs)
    deviations = de_mean(xs)
    return sum_of_squares(deviations) / (n - 1)


def standard_deviation(xs: List[float]) -> float:
    """ Стандартное отклонение - это корень квадратный из дисперсии """
    return math.sqrt(variance(xs))

def interquartile_range(xs: List[float]) -> float:
    """ Возвращает разницу между 75%-ным и 25%-ным квартилями """
    return quantile(xs, 0.75) - quantile(xs, 0.25)

def covariance(xs: List[float], ys: List[float]) -> float:
    assert len(xs) == len(ys), "xs и ys должны иметь одинаковое число элементов"
    return dot(de_mean(xs), de_mean(ys)) / (len(xs) - 1)

def correlation(xs: List[float], ys: List[float]) -> float:
    """ Измеряет степень, с которой xs и ys варьируются 
        в тандеме вокруг своих средний """
    stdev_x = standard_deviation(xs)
    stdev_y = standard_deviation(ys)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(xs, ys) / stdev_x / stdev_y
    else:
        return 0 # если вариации нет, то корреляция равна

print(correlation(num_friends, daily_hours))

