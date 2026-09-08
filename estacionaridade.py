import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams

# Configura o tamanho padrão das figuras. 15 -> x e 6 -> y
rcParams['figure.figsize'] = 15, 6

np.random.seed(10)
# Gera 41 números aleatórios com distribuição normal
# Média = 0, Desvio Padrão = 1, Tamanho = 41
dados1 = np.random.normal(0, 1, 41)
#print(dados1)

dados1 = pd.DataFrame(dados1, columns=['valores'])
#print(dados1)

# Cria um índice de datas anuais de 1980 a 2020
indice = pd.date_range(start='1980', periods=len(dados1), freq='YE')
#print(indice)

serie1 = pd.Series(dados1['valores'].values, index=indice)

serie1.plot()
plt.show()

from statsmodels.tsa.stattools import kpss, adfuller

# Teste KPSS (Kwiatkowski-Phillips-Schmidt-Shin)
# O teste KPSS é usado para verificar a estacionaridade de uma série temporal.
# A hipótese nula (H0) do teste KPSS é que a série temporal é
# estacionária, enquanto a hipótese alternativa (H1) é que a série temporal não é estacionária.
# O teste KPSS retorna dois valores principais: a estatística do teste e o valor-p
# Ha = não é estacionária: estatística do teste > valor crítico.
# Ho = é estacionária: estatística do teste <= valor crítico.
# Normalmente usa-se o nível de significância de 5% (0,05) para decidir se rejeita ou não a hipótese nula.

# result_object=True adota a API nova do statsmodels (silencia o FutureWarning).
resultado = kpss(serie1, result_object=True)
print(f"\nTeste KPSS:")
print(f"Estatística do teste: {resultado.statistic:.4f}")
print(f"p-valor: {resultado.pvalue:.4f}")
print(f"Lags: {resultado.lags}")
# Retorna um dicionário: {'10%': 0.347, '5%': 0.463, '2.5%': 0.574, '1%': 0.739}
print(f"Valores Críticos: {resultado.critical_values}")

if resultado.statistic <= resultado.critical_values['5%']:
    print("=> Não rejeita H0: a série é estacionária.")
else:
    print("=> Rejeita H0: a série não é estacionária.")



# Teste DF (Dickey-Fuller)
# O teste Dickey-Fuller é usado para verificar a estacionaridade de uma série temporal.
# A hipótese nula (H0) indica que a série não é estacionária. Estatística do teste > valor crítico.
# A hipótese alternativa (H1) indica que a série é estacionária. Estatística do teste <= valor crítico.
resultado_df = adfuller(serie1)
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



