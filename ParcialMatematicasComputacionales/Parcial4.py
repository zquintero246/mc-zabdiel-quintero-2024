import numpy as np
import matplotlib.pyplot as plt


x = np.array([1, 2, 3, 4, 5, 6, 7])
y = np.array([3.5, 4, 4.5, 5.2, 5.9, 6.5, 7.5])


coefficients = np.polyfit(x, np.log(y), 1)
a = np.exp(coefficients[1])
b = coefficients[0]


def exponential_function(x):
    return a * np.exp(b * x)


print(f"Función exponencial aproximada: y = {a} * e^({b}x)")

plt.scatter(x, y, label='Datos')
plt.plot(x, exponential_function(x), 'r', label='Ajuste exponencial')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
