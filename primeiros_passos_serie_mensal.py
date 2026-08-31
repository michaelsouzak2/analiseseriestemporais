import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams
import scipy.stats as stats # módulo de estatística do SciPy
import datetime

np.random.seed(6)
# Média = 0, Desvio Padrão = 1, Tamanho = 72
dados2 = np.random.normal(0, 1, 72)
#print(dados2)

dados2 = pd.DataFrame(dados2)
#print(dados2)

dados2.columns = ['valores']
#print(dados2.head())

#print(dados2.describe())

#Sprint(dados2.shape)

# Cria um índice de datas mensais de 2015-01 a 2020-12
# O parâmetro 'periods' define o número de períodos (neste caso, meses) 
# que queremos gerar, que é igual ao tamanho do DataFrame 'dados2' (72).
# O parâmetro 'freq' define a frequência dos períodos, 
# que neste caso é mensal ('MS' significa "Month Start", ou seja, início do mês).
indice = pd.date_range(start="2015-01", periods=72, freq="MS")
#print(indice)

# Transforma o array de datas em um DataFrame do Pandas, com uma coluna chamada 'data'.
data = pd.DataFrame(indice, columns=['data'])


# Uma alternativa ao pd.date_range() é criar um array de datas usando o NumPy.
# np.arange(72) cria um array de 0 a 71, que é adicionado à data inicial '2015-01' para gerar as datas mensais.
#data = np.array('2015-01', dtype='datetime64[M]') + np.arange(72)
#print(data)

# Transforma o array de datas em um DataFrame do Pandas, com uma coluna chamada 'data'.
#data = pd.DataFrame(data, columns=['data'])
#print(data.head())

# Só para mostrar que é possível concatenar.
#serie2 = pd.concat([data, dados2], axis=1)
#print(serie2.head())

serie2 = pd.Series(dados2['valores'].values, index=data['data'])
print(serie2)

serie2.plot()
plt.show()

# Análise de normalidade
# Gráfico Q-Q (Quantile-Quantile)
# O gráfico Q-Q é uma ferramenta gráfica para avaliar se um conjunto de dados 
# segue uma distribuição teórica específica, como a distribuição normal. 
# Ele compara os quantis dos dados observados com os quantis da 
# distribuição teórica. Se os pontos do gráfico Q-Q estiverem próximos 
# de uma linha reta, isso sugere que os dados seguem a distribuição teórica.
stats.probplot(serie2, dist="norm", plot=plt)
plt.title("Gráfico Q-Q - Série Mensal")
plt.show()

# Teste de Shapiro-Wilk
# O teste de Shapiro-Wilk é um teste estatístico que avalia a normalidade dos dados.
# Ele testa a hipótese nula de que os dados seguem uma distribuição normal.
# Nível de significância (alpha) = 0.05
# Quando o valor-p do teste de Shapiro-Wilk é menor que o nível de significância (0,05), 
# rejeitamos a hipótese nula e concluímos que os dados não seguem uma distribuição normal.
# Caso contrário, se o valor-p for maior que 0,05, não rejeitamos a hipótese nula e 
# concluímos que os dados seguem uma distribuição normal.
nivel_significancia = 0.05
shapiro_stat, shapiro_p_value = stats.shapiro(serie2)
print(f"Estatística de Shapiro-Wilk: {shapiro_stat}")
print(f"Valor-p do Teste de Shapiro-Wilk: {shapiro_p_value}")
if shapiro_p_value < nivel_significancia:
    print(f"{round(shapiro_p_value, 4)}: Rejeitamos a hipótese nula: os dados não seguem uma distribuição normal.")
else:
    print(f"{round(shapiro_p_value, 4)}: Não rejeitamos a hipótese nula: os dados seguem uma distribuição normal.")


