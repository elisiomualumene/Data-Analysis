# Amostragem Estratificada

import pandas as pd
from sklearn.model_selection import train_test_split

iris = pd.read_csv('iris.csv')
print(iris)
data = iris['variety'].value_counts()
print(data)

#x, _, y, _ = train_test_split(iris.iloc[:, 0:3], iris.iloc[:, 4], test_size=0.5, stratify=iris.iloc[:, 4])
print(train_test_split(iris.iloc[:, 0:3], iris.iloc[:, 4], test_size=0.5, stratify=iris.iloc[:, 4]))
