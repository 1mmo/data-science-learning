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
    print(younger)
    print(older)
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
