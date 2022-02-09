import enum, random


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

