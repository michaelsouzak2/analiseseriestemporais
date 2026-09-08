import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import kpss, adfuller


rcParams['figure.figsize'] = 15, 6

np.random.seed(6)
# media = 0, desvio padrão = 1, tamanho = 72
dados1 = np.random.normal(0,1,72)
# print(dados1)

serie = pd.Series(dados1)
# print(serie)

# TODO DESCOMENTAR AQUI
# serie.plot()
# plt.show()

#ACF - Autocorrelação: 
# O ACF é uma função que mede a correlação entre uma variável de uma série temporal e 
# uma versão defasada dela mesma. 
# Ele é usado para identificar padrões de dependência temporal em dados de séries temporais. 
# A função plot_acf do statsmodels é usada para visualizar o ACF, 
# mostrando os valores de autocorrelação para diferentes defasagens (lags).
# A faixa em azul representa o intervalo de confiança, 
# indicando a significância estatística das autocorrelações.
# Todos os valores de autocorrelação que caem fora dessa faixa são considerados 
# estatisticamente significativos, sugerindo que há uma relação temporal entre a variável 
# e suas versões defasadas.
# No exemplo abaixo, não há autocorrelação, pois todos os valores de autocorrelação 
# estão dentro do intervalo de confiança.
# TODO DESCOMENTAR AQUI
# plot_acf(serie, lags=8)
# plt.show()

# PACF - Autocorrelação Parcial:
# O PACF é uma função que mede a correlação entre uma variável de uma série temporal e 
# uma versão defasada dela mesma, removendo o efeito das defasagens intermediárias.
# Pode comparar lag 0 com lag 5, e assim por diante, para ver se há uma relação direta 
# entre a variável e suas versões defasadas, sem a influência das defasagens intermediárias.
# TODO DESCOMENTAR AQUI
# plot_pacf(serie, lags=30)
# plt.show()

#######################################
# ESTUDO SOBRE DADOS DE MANCHAS SOLARES
# Número médio mensal de manchas solares relativas de 1749 a 1983.

dados2 = pd.read_csv('sunspots.csv')
dados2.columns=['valores']
# print(dados2.head())

# Faz o reset do índice, que começa com 1. Nesse reset, os índices voltam a começar do zero.
# Esses números serão substituídos por datas que vão variar de 1749 à 1983.
dados2 = dados2.reset_index(drop=True)

indice = pd.date_range('1749', periods=len(dados2), freq='ME')
# print(indice)

serie2 = pd.Series(dados2['valores'].values, index=indice)
# print(serie2)

# serie2.plot()
# plt.show()

# plot_acf(serie2)
# plt.show()

# plot_pacf(serie2)
# plt.show()

resultado_kpss = kpss(serie2, result_object=True)
print(f"\nTeste KPSS:")
print(f"Estatística do teste: {resultado_kpss.statistic:.4f}")
print(f"p-valor: {resultado_kpss.pvalue:.4f}")
print(f"Valores Críticos: {resultado_kpss.critical_values}")
if resultado_kpss.statistic <= resultado_kpss.critical_values['5%']:
    print("=> Não rejeita H0: a série é estacionária.")
else:
    print("=> Rejeita H0: a série não é estacionária.")

resultado_df = adfuller(serie2)
print(f"\nTeste DF:")
print(f"Estatística do teste: {resultado_df[0]:.4f}")
print(f"p-valor: {resultado_df[1]:.4f}")
print(f"Lags: {resultado_df[2]}")
# {'1%': np.float64(-3.6055648906249997), '5%': np.float64(-2.937069375), '10%': np.float64(-2.606985625)}
print(f"Valores Críticos: {resultado_df[4]}")

if resultado_df[0] <= resultado_df[4]['5%']:
    print("=> Não rejeita H0: a série é estacionária.")
else:
    print("=> Rejeita H0: a série não é estacionária.")

# plt.show()


###########################################
# Importando datasets diretamento do Python
import statsmodels.api as sm

# mais datasets de statsmodels: https://www.statsmodels.org/devel/datasets/index.html

# Dados de manchas solares de 1700 à 2008 sobre manchas solares. 
# Fonte: National Geophysical Data Center.
manchas_solares = sm.datasets.sunspots.load_pandas().data
# print(manchas_solares)

serie3 = pd.Series(manchas_solares['SUNACTIVITY'].values, index=manchas_solares['YEAR'])
print(serie3)

serie3.plot()
# plt.show()

plot_acf(serie3, lags=45)
# plt.show()

plot_pacf(serie3, lags=30)
plt.show()

resultado_kpss = kpss(serie2, result_object=True)
print(f"\nTeste KPSS:")
print(f"Estatística do teste: {resultado_kpss.statistic:.4f}")
print(f"p-valor: {resultado_kpss.pvalue:.4f}")
print(f"Valores Críticos: {resultado_kpss.critical_values}")
if resultado_kpss.statistic <= resultado_kpss.critical_values['5%']:
    print("=> Não rejeita H0: a série é estacionária.")
else:
    print("=> Rejeita H0: a série não é estacionária.")

resultado_df = adfuller(serie2)
print(f"\nTeste DF:")
print(f"Estatística do teste: {resultado_df[0]:.4f}")
print(f"p-valor: {resultado_df[1]:.4f}")
print(f"Lags: {resultado_df[2]}")
# {'1%': np.float64(-3.6055648906249997), '5%': np.float64(-2.937069375), '10%': np.float64(-2.606985625)}
print(f"Valores Críticos: {resultado_df[4]}")

if resultado_df[0] <= resultado_df[4]['5%']:
    print("=> Não rejeita H0: a série é estacionária.")
else:
    print("=> Rejeita H0: a série não é estacionária.")