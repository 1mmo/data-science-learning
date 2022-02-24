import enum, random
import math
from matplotlib import pyplot as plt


# Enum - типизированное множество перечислимых значений.
# Мы можем им использовать для того, чтобы сделать наш код
# описательнее и читабельнее.
class Kid(enum.Enum):
    BOY = 0
    GIRL = 1

def random_kid() -> Kid:
    return random.choice([Kid.BOY, Kid.GIRL])

both_girls = 0
older_girl = 0
either_girl = 0

random.seed(0)

for _ in range(10):
    younger = random_kid()
    older = random_kid()
    if older == Kid.GIRL:
        older_girl += 1
    if older == Kid.GIRL and younger == Kid.GIRL:
        both_girls += 1
    if older == Kid.GIRL or younger == Kid.GIRL:
        either_girl += 1
    
    print(f"Both girls = {both_girls} | older girl = {older_girl}")
    print("P(both | older):", both_girls / older_girl)
    print(f"Both_girls = {both_girls} | either_girl = {either_girl}")
    print("P(both | either):", both_girls / either_girl)


def uniform_pdf(x: float) -> float:
    return 1 if x >= 0 and x < 1 else 0

def uniform_cdf(x: float) -> float:
    """ Возвращает вероятность, что равномерно
        распределенная случайная величина <= x"""
    if x < 0:
        return 0 # Равномерная величина никогда не бывает меньше 0
    elif x < 1:
        return x # Например, P(X <= 0.4) = 0.4
    else:
        return 1 # Равномерная величина всегда меньше 1

SQRT_TWO_PI = math.sqrt(2 * math.pi)

def normal_pdf(x: float, mu: float = 0, sigma: float = 1) -> float:
    return (math.exp(-(x-mu) ** 2 / 2 / sigma ** 2) / (SQRT_TWO_PI * sigma))

xs = [x / 10.0 for x in range(-50, 50)]
#plt.plot(xs, [normal_pdf(x, sigma=1) for x in xs], '-', label='мю=0, сигма=1')
#plt.plot(xs, [normal_pdf(x, sigma=2) for x in xs], '--', label='мю=0, сигма=2')
#plt.plot(xs, [normal_pdf(x, sigma=0.5) for x in xs], ':', label='мю=0, сигма=0.5')
#plt.plot(xs, [normal_pdf(x, mu=-1) for x in xs], '-.', label='мю=-1, сигма=1')
#plt.legend()
#plt.title("Различные нормальные функции плотности вероятности")
#plt.show()


def normal_cdf(x: float, mu: float = 0, sigma: float = 1) -> float:
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

xs = [x / 10.0 for x in range(-50, 50)]
plt.plot(xs, [normal_cdf(x, sigma=1) for x in xs], '-', label='мю=0, сигма=1')
plt.plot(xs, [normal_cdf(x, sigma=2) for x in xs], '--', label='мю=0, сигма=2')
plt.plot(xs, [normal_cdf(x, sigma=0.5) for x in xs], ':', label='мю=0, сигма=0.5')
plt.plot(xs, [normal_cdf(x, mu=-1) for x in xs], '-.', label='мю=-1, сигма=1')
plt.legend(loc=4) # Внизу справа
plt.title("Различные нормальные кумулятивные функции распределения")
plt.show()



