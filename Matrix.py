from typing import Tuple, Callable


def shape(A: Matrix) -> Tuple[int, int]:
    """ Возвращает (число строк А, число столбцов А) """
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0 # Число элементов в первой строке
    return num_rows, num_cols

assert shape([[1, 2, 3], [4, 5, 6]]) == (2, 3) 

def get_row(A: Matrix, i: int) -> Vector:
    """ Возвращает i-ю строку А (как тип Vector) """
    return A[i]

def get_column(A: Matrix, j: int) -> Vector:
    """ Возвращает j-й столбец А (как тип Vector) """
    return [A_i[j] for A_i in A]


def make_matrix(num_rows: int,
                num_cols: int,
                entry_fn: Callable[[int, int], float]) -> Matrix:
    """
    Возвращает матрицу размера num_rows x num_cols,
    чей (i, j)-й элемент является функцией entry_fn(i, j)
    """
    return [[entry_fn(i, j)
             for j in range(num_cols)]
             for i in range(num_rows)]

def identity_matrix(n: int) -> Matrix:
    """
    Возвращает (n x n)-матрицу тождественности,
    также именуемую единичной
    """
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)


friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]


