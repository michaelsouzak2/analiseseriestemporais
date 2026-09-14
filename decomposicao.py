import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams
import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose


rcParams['figure.figsize'] = 15,6

# Importação do dataset CO2 de MAR1958 até DEZ2001
concentracao = sm.datasets.co2.load_pandas().data
# print(concentracao)

serie = pd.Series(concentracao['co2'].values, index=concentracao.index)
# print(serie)

# Existem 2284 obsrevações registradas a cada semana, de 7 em 7 dias, desde 1958 até 2001.
# Em algumas semanas não foram realizadas as observações. Dessa forma, existem alguns dias 
# em que a medição ficou nula. 
# Para verificar quais observações ficaram como null, basta, realizar o comando abaixo.
# Observa-se-á que são 59 observações no total, número não significativo para o total.
# Essas ausências serão removidas.
print(concentracao.isnull())

# Remove os valores nulos (59 no total)
concentracao = concentracao.dropna()

serie = pd.Series(concentracao['co2'].values, index=concentracao.index)
serie.plot()

# period=7 -> Significa que as observações ocorrem a cada sete dias.
decomposicao = seasonal_decompose(serie, period=30)
decomposicao.plot()

plt.show()

