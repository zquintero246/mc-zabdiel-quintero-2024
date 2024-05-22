import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5, 6, 7])
y = np.array([3.5, 4, 4.5, 5.2, 5.9, 6.5, 7.5])

m, b = np.polyfit(x, y, 1)

print("Pendiente (m):", m)
print("Ordenada al origen (b):", b)
print("Ecuación de la línea recta: y =", m, "x +", b)


def f(x):
    return m * x + b


plt.scatter(x, y, color='red', label='Datos')


plt.plot(x, f(x), color='blue', label='Ajuste lineal')


plt.xlabel('x')
plt.ylabel('y')
plt.legend()


plt.grid(True)
plt.show()
