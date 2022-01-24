from matplotlib import pyplot as plt
from collections import Counter


grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]

histogram = Counter(min(grade // 10 * 10, 90) for grade in grades)

plt.bar([x + 5 for x in histogram.keys()],
        list(histogram.values()),
        10)
plt.axis([-5, 105, 0, 5])

plt.xticks([10 * i for i in range(11)]) # Метки по оси x: 0, 10, ..., 100
plt.xlabel("Д")
plt.ylabel("Число студентов")
plt.title("Распределение оценок за экзамен №1")
plt.show()
