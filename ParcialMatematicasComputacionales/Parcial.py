import numpy as np 



def suma_matrices(matriz1, matriz2):
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        return "Las matrices no tienen las mismas dimensiones"
    
    resultado = []
    for i in range(len(matriz1)):
        fila = []
        for j in range(len(matriz1[0])):
            fila.append(matriz1[i][j] + matriz2[i][j])
        resultado.append(fila)
    
    return resultado

def resta_matrices(matriz1, matriz2):
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        return "Las matrices no tienen las mismas dimensiones"
    
    resultado = []
    for i in range(len(matriz1)):
        fila = []
        for j in range(len(matriz1[0])):
            fila.append(matriz1[i][j] - matriz2[i][j])
        resultado.append(fila)
    
    return resultado

def multiplicacion_matrices(matriz1, matriz2):
    if len(matriz1[0]) != len(matriz2):
        return "El número de columnas de la primera matriz no coincide con el número de filas de la segunda matriz"
    
    resultado = []
    for i in range(len(matriz1)):
        fila = []
        for j in range(len(matriz2[0])):
            suma = 0
            for k in range(len(matriz2)):
                suma += matriz1[i][k] * matriz2[k][j]
            fila.append(suma)
        resultado.append(fila)
    
    return resultado

def transponer_matriz(matriz):
    resultado = []
    for j in range(len(matriz[0])):
        fila = []
        for i in range(len(matriz)):
            fila.append(matriz[i][j])
        resultado.append(fila)
    
    return resultado

def matriz_inversa(matriz):
    try:
        inversa = np.linalg.inv(matriz)
        return inversa
    except np.linalg.LinAlgError:
        return "La matriz no es invertible"
    

# Ejemplo de uso
matriz_a = [[3, 1, 0],
            [4, 2, -1],
            [1, 3, -0]]

matriz_b = [[5, 0],
            [-3, -1],
            [0, 2]]

matriz_c = [[2, 0, -1],
            [3, 0, 1],
            [7, -2, 3]]


print("\nProducto de matrices:")
print(multiplicacion_matrices(matriz_a, matriz_b))

print("\nInversa de la matriz:")
print(matriz_inversa(matriz_c))
