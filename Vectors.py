import math
from typing import List


Vector =  List[float]

height_weight_age = [175, 68, 40]

grades  = [95, 80, 75, 62]

def add(v: Vector, w: Vector) -> Vector:
    """ Складывает соответствующие элементы """
    assert len(v) == len(w), "векторы должны иметь одинаковую длину"

    return [v_i + w_i for v_i, w_i in zip(v, w)]

assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]\

def subtract(v: Vector, w: Vector) -> Vector:
    """ Вычитает соответствующие элементы """
    assert len(v) == len(w), "векторы должны иметь одинаковую длину"

    return [v_i - w_i for v_i, w_i in zip(v, w)]

assert subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]

def vector_sum(vectors: List[Vector]) -> Vector:
    """ Суммирует все соответствующие элементы """
    # Проверить, что все векторы не пустые
    assert vectors, "векторы не предоставлены"

    # Проверить, что все векторы имеют одинаковый размер
    num_elements = len(vectors[0])

    assert all(len(v) == num_elements for v in vectors), "разные размеры"

    # i-й элемент результата является суммой каждого элемента vector[i]
    return [sum(vector[i] for vector in vectors) 
            for i in range(num_elements)]

vector =  vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]])
print(vector)

def scalar_multiply(c: float, v: Vector) -> Vector:
    """ Умножает каждый эелемент на с """
    return [c * v_i for v_i in v]

assert scalar_multiply(2, [1, 2, 3])

def vector_mean(vectors: List[Vector]) -> Vector:
    """ Вычисляет поэлементное среднее арифметическое """
    n = len(vectors)
    print(n)
    return scalar_multiply(1/n, vector_sum(vectors))

def dot(v: Vector, w: Vector) -> float:
    """ Вычисляет v_i * w_i + ... + v_n * w_n """
    assert len(v) == len(w), "векторы должны иметь одинаковую длину"

    return sum(v_i * w_i for v_i, w_i in zip(v, w))

assert dot([1, 2, 3], [4, 5, 6]) == 32

def sum_of_squares(v: Vector) -> float:
    """ Возвращает v_i * v_i + ... + v_n * v_n """
    return dot(v, v)

assert sum_of_squares([1, 2, 3]) == 14

def magnitude(v: Vector) -> float:
    """ Возвращает магнитуду (или длину) вектора v """
    # math.sqrt - это функция квадратного корня
    return math.sqrt(sum_of_squares(v))
