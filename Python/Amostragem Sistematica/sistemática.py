# Amostras Sistemáticas

import numpy as np
import pandas as pd
from math import ceil

populacao = 150
amostra = 15

k = ceil(populacao / amostra)
# print(k)

r = np.random.randint(low=1, high=k + 1, size=1)
# print(r)

acumulator = r[0]

sorter = []

for i in range(amostra):
    sorter.append(acumulator)
    acumulator += k
    # print(acumulator)

base = pd.read_csv('../Amostragem/iris.csv')
final_base = base.loc[sorter]
print(final_base)
