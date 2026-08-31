import matplotlib.pyplot as plt
import numpy as np

velocidades = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25]


# Quartis
q1 = np.percentile(velocidades, 25)
q2 = np.percentile(velocidades, 50)
q3 = np.percentile(velocidades, 75)

print("Q1:", q1)
print("Q2:", q2)
print("Q3:", q3)

# Amplitude interquartis
aiq = q3 - q1

print("AIQ:", aiq)

# Limites inferiores e superiores para verificação de outliers
limite_inferior = q1 - 1.5 * aiq
limite_superior = q3 + 1.5 * aiq

print("Limite inferior:", limite_inferior)
print("Limite superior:", limite_superior)

plt.boxplot(velocidades)
plt.ylabel('Velocidade (nós)')
plt.title("Distribuição das velocidades das EMB")


plt.show()

