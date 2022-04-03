# Amostragem Estratificada

import pandas as pd
# from sklearn.model_selection import train_test_split
iris = pd.read_csv('iris.csv')
data = iris['variety'].value_counts()
print(data)
