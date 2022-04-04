# Amostragem Estratificada

import pandas as pd
from sklearn.model_selection import train_test_split

iris = pd.read_csv('iris.csv')
data = iris['variety'].value_counts()

x, _, y, _ = train_test_split(iris.iloc[:, 0:4], iris.iloc[:, 4], test_size=0.5, stratify=iris.iloc[:, 4])
print(y.value_counts())

infert = pd.read_csv('infert.csv')
split = infert['education'].value_counts()
print(split)

x1, _, y1, _ = train_test_split(infert.iloc[:, 2:9], infert.iloc[:, 1], test_size=0.6, stratify=infert.iloc[:, 1])
print(y1.value_counts())
