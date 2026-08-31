import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams
import scipy.stats as stats # módulo de estatística do SciPy
import datetime


np.random.seed(20)
dados4 = np.random.normal(0, 1, 164)

dados4 = pd.DataFrame(dados4, columns=['valores'])

print(dados4.describe())
print(dados4.shape)

# Cria um índice de datas trimestrais de 1980-01-01 a 2020-12-31
# O parâmetro 'periods' define o número de períodos (neste caso, trimestres) que queremos gerar, que é igual ao tamanho do DataFrame 'dados4' (164).
# O parâmetro 'freq' define a frequência dos períodos, que neste caso é trimestral ('Q' significa "Quarter", ou seja, trimestre).
indice4 = pd.date_range(start="1980-01", periods=len(dados4), freq="QE")
#print(indice4) 

serie4 = pd.Series(dados4['valores'].values, index=indice4)
#print(serie4)

serie4.plot()
plt.title("Série Trimestral de 1980 a 2020")
plt.xlabel("Ano")
plt.ylabel("Valores")
plt.show()

# Análise de normalidade
# Gráfico Q-Q (Quantile-Quantile)
stats.probplot(serie4, dist="norm", plot=plt)
plt.title("Gráfico Q-Q - Série Trimestral")
plt.show()

# Teste de Shapiro-Wilk
e, p = stats.shapiro(serie4)
print("Estatística de teste:", e)
print("Valor-p:", p)

