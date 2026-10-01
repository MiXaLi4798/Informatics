from random import randint
from matplotlib import pyplot as plt
import numpy as np

fig = plt.figure(figsize=(1280, 720, 'px'))
axes = fig.subplots(2)

x = 0
path = []
standard_deviations = []
for _ in range(1000):
    if randint(0, 1):
        x += 1
    else:
        x -= 1
    path.append(x)
    standard_deviations.append(np.sqrt(1 / 1000 * sum((np.array(path) - np.mean(path)) ** 2)))
axes[0].plot(range(1, 1001), path, color='black', label='x(N)')
axes[0].set_title('Зависимость координаты частицы от количества шагов')
axes[0].set_xlabel('Количество шагов N')
axes[0].set_ylabel('Координата частицы x')
axes[0].set_xlim(0, 1001)
axes[0].plot(range(1, 1001), standard_deviations, color='red', label='σ(N)')
axes[0].legend()

paths = []

for _ in range(1000):
    x = 0
    path = []
    for __ in range(1000):
        if randint(0, 1):
            x += 1
        else:
            x -= 1
        path.append(x)
    paths.append(path[-1])

axes[1].hist(paths, bins=len(set(paths)))
axes[1].set_title('Количество частиц с координатой x после 1000 шагов в зависимости от координаты x')
axes[1].set_xlabel('Координата x')
axes[1].set_ylabel('Количество частиц с координатой x')

plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.1)
fig.tight_layout()

plt.show()
