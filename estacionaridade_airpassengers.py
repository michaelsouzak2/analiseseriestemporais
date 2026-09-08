import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams
from statsmodels.tsa.stattools import kpss, adfuller


rcParams['figure.figsize'] = 15, 6

# DATASET IMPORTADO
# Totais mensais de passageiros aéreos internacionais (em milhares) de 1949 a 1960.
serie2 = pd.read_csv('AirPassengers.csv')
print(serie2.head())

serie2 = pd.Series(serie2['#Passengers'].values, index=serie2['Month'])
print(serie2.head())

serie2.plot()
plt.show()

# Hipótese nula (H0): a série é estacionária. estatística do teste <= valor crítico.
# Hipótese alternativa (H1): a série não é estacionária. estatística do teste > valor crítico.
resultado_kpss = kpss(serie2, result_object=True)
print(f"\nTeste KPSS:")
print(f"Estatística do teste: {resultado_kpss.statistic:.4f}")
print(f"p-valor: {resultado_kpss.pvalue:.4f}")
print(f"Valores Críticos: {resultado_kpss.critical_values}")
if resultado_kpss.statistic <= resultado_kpss.critical_values['5%']:
    print("=> Não rejeita H0: a série é estacionária.")
else:
    print("=> Rejeita H0: a série não é estacionária.")


# Hipótese nula (H0): a série não é estacionária. estatística do teste > valor crítico.
# Hipótese alternativa (H1): a série é estacionária. estatística do teste <= valor crítico.
resultado_df = adfuller(serie2)
print(f"\nTeste DF:")
print(f"Estatística do teste: {resultado_df[0]:.4f}")
print(f"p-valor: {resultado_df[1]:.4f}")
print(f"Valores Críticos: {resultado_df[4]}")
if resultado_df[0] <= resultado_df[4]['5%']:
    print("=> Não rejeita H0: a série é estacionária.")
else:
    print("=> Rejeita H0: a série não é estacionária.")
