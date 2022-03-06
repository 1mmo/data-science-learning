import random
from Vectors import (distance, add, 
                     scalar_multiply, Vector)

"""
Проверка фукнции sum_of_squares: v_i * v_i + ... + v_n * v_n
на нахождение минимума с помощью градиента.
Мы будем использовать градиенты для отыскания минимума
среди всех трехмерных векторов. Выберем случайную отправную точку
и крошечными шажками начнем двигаться в направлении,
противоположном градиенту, до тех пор, пока не достигнем точки,
где градиент будет очень мал
"""

def gradient_step(v: Vector, gradient: Vector, step_size: float) -> Vector:
    """ Движемся с шагом 'step_size' в направлении
        градиента 'gradient' от 'v' """

    assert len(v) == len(gradient)
    step = scalar_multiply(step_size, gradient)
    return add(v, step)

def sum_of_squares_gradient(v: Vector) -> Vector:
    return [2 * v_i for v_i in v]

# Подобрать случайную отправную точку
v = [random.uniform(-10, 10) for i in range(3)]

for epoch in range(1000):
    grad = sum_of_squares_gradient(v) # Вычислить градиент в v
    v = gradient_step(v, grad, -0.01) # Сделать отрицательный
                                      # градиентный шаг

    #print(epoch, v)




