# SepalLength[1] от SepalWidth[2], SepalLength[1] от PetalLength[3], SepalLength[1] от PetalWidth[4]
# PetalLength[3] от PetalWidth[4], PetalLength[3] от SepalWidth[2], SepalWidth[2] от PetalWidth[4]

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

data = pd.read_csv('iris_data.csv')
fig = plt.figure(figsize=(1280, 720, 'px'), label='Зависимости длин и ширин лепестков и чашелистников')
axes = fig.subplots(2, 3)

# верхний левый
data001 = data[data['Species'] == 'Iris-setosa'].sort_values(by='SepalWidthCm')
axes[0, 0].scatter(data001['SepalWidthCm'], data001['SepalLengthCm'], color='blue', label='Iris-setosa', s=20)

data002 = data[data['Species'] == 'Iris-versicolor'].sort_values(by='SepalWidthCm')
axes[0, 0].scatter(data002['SepalWidthCm'], data002['SepalLengthCm'], color='red', label='Iris-versicolor', s=20)

data003 = data[data['Species'] == 'Iris-virginica'].sort_values(by='SepalWidthCm')
axes[0, 0].scatter(data003['SepalWidthCm'], data003['SepalLengthCm'], color='green', label='Iris-virginica', s=20)

axes[0, 0].set_xlabel('Sepal Width, cm')
axes[0, 0].set_ylabel('Sepal Length, cm')

# верхний центральный
data011 = data[data['Species'] == 'Iris-setosa'].sort_values(by='PetalLengthCm')
axes[0, 1].scatter(data011['PetalLengthCm'], data011['SepalLengthCm'], color='blue', label='Iris-setosa', s=20)

data012 = data[data['Species'] == 'Iris-versicolor'].sort_values(by='PetalLengthCm')
axes[0, 1].scatter(data012['PetalLengthCm'], data012['SepalLengthCm'], color='red', label='Iris-versicolor', s=20)

data013 = data[data['Species'] == 'Iris-virginica'].sort_values(by='PetalLengthCm')
axes[0, 1].scatter(data013['PetalLengthCm'], data013['SepalLengthCm'], color='green', label='Iris-virginica', s=20)

axes[0, 1].set_xlabel('Petal Length, cm')
axes[0, 1].set_ylabel('Sepal Length, cm')
axes[0, 1].set_title('Зависимости длин и ширин лепестков и чашелистников')

# МНК для верхнего центрального
data_lsm01 = data.sort_values(by='PetalLengthCm')
lsm01 = np.polyfit(data_lsm01['PetalLengthCm'], data_lsm01['SepalLengthCm'], 1)
k01 = lsm01[0]
b01 = lsm01[1]
axes[0, 1].plot(data_lsm01['PetalLengthCm'], k01 * np.array(data_lsm01['PetalLengthCm']) + b01, color='black', label='Аппроксимирующая прямая\nпо МНК')
axes[0, 1].text(2.1, 6.3, f'k = {round(k01, 3)}\nb = {round(b01, 3)}')

axes[0, 1].legend(fontsize='x-small')

# верхний правый
data021 = data[data['Species'] == 'Iris-setosa'].sort_values(by='PetalWidthCm')
axes[0, 2].scatter(data021['PetalWidthCm'], data021['SepalLengthCm'], color='blue', label='Iris-setosa', s=20)

data022 = data[data['Species'] == 'Iris-versicolor'].sort_values(by='PetalWidthCm')
axes[0, 2].scatter(data022['PetalWidthCm'], data022['SepalLengthCm'], color='red', label='Iris-versicolor', s=20)

data023 = data[data['Species'] == 'Iris-virginica'].sort_values(by='PetalWidthCm')
axes[0, 2].scatter(data023['PetalWidthCm'], data023['SepalLengthCm'], color='green', label='Iris-virginica', s=20)

axes[0, 2].set_xlabel('Petal Width, cm')
axes[0, 2].set_ylabel('Sepal Length, cm')

# МНК для верхнего правого
data_lsm02 = data.sort_values(by='PetalWidthCm')
lsm02 = np.polyfit(data_lsm02['PetalWidthCm'], data_lsm01['SepalLengthCm'], 1)
k02 = lsm02[0]
b02 = lsm02[1]
axes[0, 2].plot(data_lsm02['PetalWidthCm'], k02 * np.array(data_lsm02['PetalWidthCm']) + b02, color='black')
axes[0, 2].text(0.3, 6.8, f'k = {round(k02, 3)}\nb = {round(b02, 3)}')

# нижний левый
data101 = data[data['Species'] == 'Iris-setosa'].sort_values(by='PetalWidthCm')
axes[1, 0].scatter(data101['PetalWidthCm'], data101['PetalLengthCm'], color='blue', label='Iris-setosa', s=20)

data102 = data[data['Species'] == 'Iris-versicolor'].sort_values(by='PetalWidthCm')
axes[1, 0].scatter(data102['PetalWidthCm'], data102['PetalLengthCm'], color='red', label='Iris-versicolor', s=20)

data103 = data[data['Species'] == 'Iris-virginica'].sort_values(by='PetalWidthCm')
axes[1, 0].scatter(data103['PetalWidthCm'], data103['PetalLengthCm'], color='green', label='Iris-virginica', s=20)

axes[1, 0].set_xlabel('Petal Width, cm')
axes[1, 0].set_ylabel('Petal Length, cm')

# МНК для нижнего левого
data_lsm10 = data.sort_values(by='PetalWidthCm')
lsm10 = np.polyfit(data_lsm10['PetalWidthCm'], data_lsm10['PetalLengthCm'], 1)
k10 = lsm10[0]
b10 = lsm10[1]
axes[1, 0].plot(data_lsm10['PetalWidthCm'], k10 * np.array(data_lsm10['PetalWidthCm']) + b10, color='black')
axes[1, 0].text(0.3, 5, f'k = {round(k10, 3)}\nb = {round(b10, 3)}')

# нижний центральный
data111 = data[data['Species'] == 'Iris-setosa'].sort_values(by='SepalWidthCm')
axes[1, 1].scatter(data111['SepalWidthCm'], data111['PetalLengthCm'], color='blue', label='Iris-setosa', s=20)

data112 = data[data['Species'] == 'Iris-versicolor'].sort_values(by='SepalWidthCm')
axes[1, 1].scatter(data112['SepalWidthCm'], data112['PetalLengthCm'], color='red', label='Iris-versicolor', s=20)

data113 = data[data['Species'] == 'Iris-virginica'].sort_values(by='SepalWidthCm')
axes[1, 1].scatter(data113['SepalWidthCm'], data113['PetalLengthCm'], color='green', label='Iris-virginica', s=20)

axes[1, 1].set_xlabel('Sepal Width, cm')
axes[1, 1].set_ylabel('Petal Length, cm')

# нижний правый
data121 = data[data['Species'] == 'Iris-setosa'].sort_values(by='PetalWidthCm')
axes[1, 2].scatter(data121['PetalWidthCm'], data121['SepalWidthCm'], color='blue', label='Iris-setosa', s=20)

data122 = data[data['Species'] == 'Iris-versicolor'].sort_values(by='PetalWidthCm')
axes[1, 2].scatter(data122['PetalWidthCm'], data122['SepalWidthCm'], color='red', label='Iris-versicolor', s=20)

data123 = data[data['Species'] == 'Iris-virginica'].sort_values(by='PetalWidthCm')
axes[1, 2].scatter(data123['PetalWidthCm'], data123['SepalWidthCm'], color='green', label='Iris-virginica', s=20)

axes[1, 2].set_xlabel('Petal Width, cm')
axes[1, 2].set_ylabel('Sepal Width, cm')

plt.subplots_adjust(left=0.05, bottom=0.1, right=0.95, top=0.95)
plt.show()
