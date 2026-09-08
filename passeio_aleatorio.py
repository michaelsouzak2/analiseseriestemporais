import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams
from random import sample, random

rcParams['figure.figsize'] = 15, 6

# De um conjunto de 100 números, seleciona aleatoriamente 41 números distintos.
# sample -> Amostra
dados1 = sample(range(100), k=41)
# print(dados1)

anos = list(range(1980, 2021))
# print(anos)

serie1 = pd.Series(dados1, index=anos)
# print(serie1)

#serie1.plot()
#plt.show()

# random() -> Gera um número aleatório entre 0 e 1.
serie2 = list()
serie2.append(-1 if random() < 0.5 else 1)
for i in range(1, 1000):
    movimento = -1 if random() < 0.5 else 1
    valor = serie2[i-1] + movimento
    serie2.append(valor)

serie2 = pd.Series(serie2)
serie2.plot()
plt.show()