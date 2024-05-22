import matplotlib.pyplot as plt
import numpy as np

def lagrange_interpolation(x_values, y_values, x):
    """
    Calculate Lagrange interpolation polynomial value at point x.
    
    Args:
    x_values: List of x values of the data points.
    y_values: List of y values of the data points.
    x: Point at which to evaluate the polynomial.
    
    Returns:
    Interpolated value at point x.
    """
    n = len(x_values)
    result = 0.0
    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if j != i:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term
    return result

# Datos de ejemplo
x_values = [0, 1, 2, 3, 4]
y_values = [1.5, 2, 3.5, 1.8, 0]

# Puntos a evaluar
point_to_evaluate = 2.7

# Interpolación de Lagrange
lagrange_degree_1 = lagrange_interpolation(x_values[:2], y_values[:2], point_to_evaluate)
lagrange_degree_2 = lagrange_interpolation(x_values[:3], y_values[:3], point_to_evaluate)
lagrange_degree_3 = lagrange_interpolation(x_values[:4], y_values[:4], point_to_evaluate)
lagrange_degree_4 = lagrange_interpolation(x_values, y_values, point_to_evaluate)

# Resultados
print("Valor estimado de f(2.7):")
print(f"Grado 1: {lagrange_degree_1}")
print(f"Grado 2: {lagrange_degree_2}")
print(f"Grado 3: {lagrange_degree_3}")
print(f"Grado 4: {lagrange_degree_4}")

# Generar puntos para graficar los polinomios
x_range = np.linspace(0, 4, 100)
y_range_degree_1 = lagrange_interpolation(x_values[:2], y_values[:2], x_range)
y_range_degree_2 = lagrange_interpolation(x_values[:3], y_values[:3], x_range)
y_range_degree_3 = lagrange_interpolation(x_values[:4], y_values[:4], x_range)
y_range_degree_4 = lagrange_interpolation(x_values, y_values, x_range)

# Graficar los polinomios interpolados
plt.figure(figsize=(12, 8))
plt.plot(x_range, y_range_degree_1, label='Grado 1')
plt.plot(x_range, y_range_degree_2, label='Grado 2')
plt.plot(x_range, y_range_degree_3, label='Grado 3')
plt.plot(x_range, y_range_degree_4, label='Grado 4')
plt.scatter(x_values, y_values, color='red', label='Datos')
plt.scatter(point_to_evaluate, lagrange_degree_1, color='blue')
plt.scatter(point_to_evaluate, lagrange_degree_2, color='orange')
plt.scatter(point_to_evaluate, lagrange_degree_3, color='green')
plt.scatter(point_to_evaluate, lagrange_degree_4, color='purple')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Interpolación de Lagrange')
plt.legend()
plt.grid(True)
plt.show()
