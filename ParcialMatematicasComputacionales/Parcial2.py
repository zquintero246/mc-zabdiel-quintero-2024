import numpy as np
import matplotlib.pyplot as plt

def polynomial_regression(x, y, degree):
    X = np.vstack([x**i for i in range(degree, -1, -1)]).T
    coeffs = np.linalg.lstsq(X, y, rcond=None)[0]
    return coeffs

def calculate_polynomial(coeffs, x):
    y_pred = sum([coeffs[i] * x**(len(coeffs)-i-1) for i in range(len(coeffs))])
    return y_pred

x = np.array([1, 2, 3, 4, 5, 6, 7])
y = np.array([3.5, 4, 4.5, 5.2, 5.9, 6.5, 7.5])
degree = 2

coefficients = polynomial_regression(x, y, degree)
print("Coeficientes del polinomio de segundo grado:")
print(coefficients)

equation = "y = "
for i in range(len(coefficients)):
    equation += f"{coefficients[i]}x^{len(coefficients)-i-1}"
    if i != len(coefficients)-1:
        equation += " + "
print("Ecuacion del polinomio de segundo grado:")
print(equation)


plt.scatter(x, y, color='red', label='Datos')


def f(x):
    return sum([coefficients[i] * x**(len(coefficients)-i-1) for i in range(len(coefficients))])


x_values = np.linspace(min(x), max(x), 100)


plt.plot(x_values, f(x_values), color='blue', label='Polinomio de segundo grado')


plt.xlabel('x')
plt.ylabel('y')
plt.legend()


plt.grid(True)
plt.show()
