# Amostragem: Primeira Aula de análise de Dados
# Amostragem Simples
import pandas as pd
import numpy as np
base = pd.read_csv('iris.csv')

print(base)

amostra = np.random.choice(a=[0, 1], size=[150], replace=True, p=[0.5, 0.5])

print(len(amostra[amostra == 1]))

print(len(amostra[amostra == 0]))
