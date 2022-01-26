from matplotlib import pyplot as plt


relationship = [5, 17, 18, 24]
days = [27, 21, 23, 21]

plt.scatter(relationship, days)
plt.axis('equal')
plt.xlabel("Срок отношений в месяцах")
plt.ylabel("Дни в Моздоке")
plt.show()
