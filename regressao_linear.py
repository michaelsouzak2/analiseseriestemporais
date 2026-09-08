import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

dados = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [1.3, 1.8, 3.5, 4, 4.6]
})

dados['y_reta'] = dados['x']

reg = LinearRegression()
reg.fit(dados['x'].values.reshape(-1, 1), dados['y'])

m = reg.coef_
b = reg.intercept_
print(f'Coeficiente angular (m): {m}')
print(f'Coeficiente linear (b): {b}')

fig, ax = plt.subplots()
ax.scatter(dados['x'], dados['y'])
ax.plot(dados['x'], dados['y_reta'], color='red', linestyle='--')

x = dados['x'].values
y = m * x + b
ax.plot(x, y, color='blue', label='Regressão Linear')

#plt.show()

# Vai prever os valores de y para os valores de x fornecidos
dados['y_pred'] = reg.predict(dados['x'].values.reshape(-1, 1))
dados['residuos'] = dados['y'] - dados['y_pred']

