import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams
import scipy.stats as stats # módulo de estatística do SciPy
import datetime


np.random.seed(12)
# Gera 731 números aleatórios com distribuição normal
# Média = 1, Desvio Padrão = 2, Tamanho = 731
dados3 = np.random.normal(1, 2, 731)

dados3 = pd.DataFrame(dados3, columns=['valores'])

print(dados3.describe())
print(dados3.shape)

# Cria um índice de datas diárias de 2019-01-01 a 2020-12-31
# O parâmetro 'periods' define o número de períodos (neste caso, dias) que queremos gerar, que é igual ao tamanho do DataFrame 'dados3' (731).
# O parâmetro 'freq' define a frequência dos períodos, que neste caso é diária ('D' significa "Day", ou seja, dia).
indice3 = pd.date_range(start="2019-01-01", periods=len(dados3), freq="D")
#print(indice3)

serie3 = pd.Series(dados3['valores'].values, index=indice3)
print(serie3)

serie3.plot()
plt.show()


# Análise de normalidade
# Gráfico Q-Q (Quantile-Quantile)
stats.probplot(serie3, dist="norm", plot=plt)
plt.title("Gráfico Q-Q")
plt.xlabel("Quantiles Teóricos")
plt.ylabel("Quantiles Amostrais")
plt.show()


# Teste de Shapiro-Wilk
e, p = stats.shapiro(serie3)
print("Estatística de teste:", e)
print("Valor-p:", p)
