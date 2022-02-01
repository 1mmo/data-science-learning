import matplotlib.pyplot as plt
from collections import Counter
from typing import List


# Число друзей
num_friends = [100, 49, 41, 40, 25]

friend_counts = Counter(num_friends)
print(friend_counts)
xs = range(101)
ys = [friend_counts[x] for x in xs]
print(ys)

plt.bar(xs, ys)
plt.axis([0, 101, 0, 25])
plt.title("Гистограмма количеств друзей")
plt.xlabel('Число друзей')
plt.ylabel('Число людей')
plt.show()

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

print(mean(num_friends))


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

print(mode(num_friends))
