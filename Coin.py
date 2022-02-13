from typing import Tuple
import math

from Probability import normal_cdf 


# Аппроксимация биномиальной сл величины нормальным распределением
def normal_approximation_to_binomial(n: int, p: float) -> Tuple[float, float]:
    """ Возвращает mu и sigma, соответствующие binomial(n, p) """
    mu = p * n
    sigma = math.sqrt(p * (1 - p) * n)
    return mu, sigma

# Нормальная функция CDF (normal_cdf) - это вероятность,
# что переменная лежит ниже порога
normal_probability_below = normal_cdf

def normal_probability_above(lo: float, mu: float = 0, sigma: float = 1) -> float:
    """ Вероятность, что N(mu, sigma) выше, чем lo. """
    return 1 - normal_cdf(lo, mu, sigma)

# Она лежит между, если она меньше, чем hi, но не меньше, чем lo
def normal_probability_between(lo: float, hi: float, 
                               mu: float = 0, sigma: float = 1) -> float:
    """ Вероятность, что N(mu, sigma) между lo и hi. """
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)

# Она лежит за пределами, если она не лежит между
    def normal_probaЬility_outside(lo: float,
                                   hi: float,
                                   mu: float = О,
                                   sigma: float = 1) -> float:
    """Вероятность, что N(mu, sigma) не лежит между lo и hi."""
    return 1 - normal_probaЬility_between(lo, hi, mu, sigma)

