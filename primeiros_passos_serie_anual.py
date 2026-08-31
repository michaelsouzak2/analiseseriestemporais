import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams
import scipy.stats as stats # módulo de estatística do SciPy


# Configura o tamanho padrão das figuras. 15 -> x e 6 -> y
rcParams['figure.figsize'] = 15, 6 

# Série anual de 1980 a 2020

# Define a semente para o gerador de números aleatórios
# A semente 10 sempre sejam os mesmos, independente de quantas vezes o código seja executado.
np.random.seed(10)
# Gera 41 números aleatórios com distribuição normal
# Média = 0, Desvio Padrão = 1, Tamanho = 41
dados1 = np.random.normal(0, 1, 41)  
#print(dados1)
#print(type(dados1))  # <class 'numpy.ndarray'>

serie = pd.Series(dados1)
#print(serie)
#print(type(serie))  # <class 'pandas.core.series.Series'>

# São os mesmos valores.
#print(dados1[0])
#print(serie[0])

#serie.plot()
#plt.show()

dados1 = pd.DataFrame(dados1)
print(dados1)

dados1.columns = ['valores']

# Mostra os 5 primeiros valores do DataFrame
print(dados1.head())

# 41 linhas e 1 coluna
print(dados1.shape)

"""
count  41.000000 -> Contagem
mean    0.183670 -> Média
std     0.964847 -> Desvio Padrão
min    -1.977728 -> Mínimo
25%    -0.337632 -> 25º Percentil
50%     0.195013 -> 50º Percentil
75%     0.715279 -> 75º Percentil
max     2.384967 -> Máximo
"""
print(dados1.describe())

# Cria um índice de datas anuais de 1980 a 2020
# O parâmetro 'periods' define o número de períodos 
# (neste caso, anos) que queremos gerar, que é igual ao 
# tamanho do DataFrame 'dados1' (41). 
# O parâmetro 'freq' define a frequência dos períodos, 
# que neste caso é anual ('YE').
indice = pd.date_range('1980', periods=len(dados1), freq='YE')
print(indice)

# Imprime as linhas da coluna valores em formato de lista.
print(dados1['valores'].values) 
# Imprime uma representação do Dataframe.
print(dados1)

serie1 = pd.Series(dados1['valores'].values, index=indice)
print(serie1)

#serie1.plot()
#plt.show()

# Verificação gráfica para verificar normalidade.
stats.probplot(serie1, dist="norm", plot=plt)
plt.title("Normal QQ plot")
plt.show()

# Verificação estatística para verificar normalidade.
# O teste de Shapiro-Wilk é um teste estatístico que avalia a normalidade dos dados. 
# Ele testa a hipótese nula de que os dados seguem uma distribuição normal.
# O teste retorna dois valores: o valor estatístico do teste (statistic ou W ou e) e o valor p (p-value). 
# statistic é uma medida da diferença entre a distribuição dos dados e a distribuição normal teórica.
# Se o valor p for menor que um nível de significância (geralmente 0,05), rejeitamos a hipótese nula e concluímos que os dados não seguem uma distribuição normal.
# Caso contrário, se o valor p for maior que o nível de significância, não rejeitamos a hipótese nula e concluímos que os dados podem seguir uma distribuição normal.
e, p = stats.shapiro(serie1)
nivel_significancia = 0.05
print("Estatística do teste de Shapiro-Wilk:", e)
print("Valor p do teste de Shapiro-Wilk:", p)
if p > nivel_significancia:
    print(f"Com {round(p, 4)} maior que {nivel_significancia}, não rejeitamos H0. Portanto, não encontramos evidências estatísticas suficientes para afirmar que os dados não são normais.")
else:
    print(f"Com {round(p, 4)} menor que {nivel_significancia}, rejeitamos H0. Portanto, encontramos evidências estatísticas suficientes para afirmar que os dados não são normais.")

