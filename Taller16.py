import copy

def imprimirSistema(a, b, etiqueta):
    n = len(b)
    print(etiqueta)
    for i in range(n):
        for j in range(n):
            print(a[i][j], end = " ")
        print("|", b[i])
    print()

def gaussJordan(ao, bo):
    a = copy.deepcopy(ao)
    b = copy.deepcopy(bo)

    n = len(b)
    imprimirSistema(a, b, "Matriz inicial")
    for i in range(n):
        pivote = a[i][i]
        if(pivote == 0):
            for j in range(i+1, n):
                pivoteCorreccion = a[j][i]
                if(pivoteCorreccion != 0):
                    tempA = a[j]
                    tempB = b[j]
                    a[j] = a[i]
                    b[j] = b[i]
                    a[i] = tempA
                    b[i] = tempB
                    break
        pivote = a[i][i]
        print("pivote: " + str(pivote) + ", i: " + str(i))
        
        for j in range(n):
            a[i][j] /= pivote
            b[i][j] /= pivote
        imprimirSistema(a, b, "División")

    
        for k in range(n):
            if i != k:
                #Se reduce
                valorAux = -a[k][i]
                for j in range(n):
                    a[k][j] += a[i][j] * valorAux
                    b[k][j] += b[i][j] * valorAux
        imprimirSistema(a, b, "Reducción")
    
    return b

print("Caso 1:")

a = [[3, 2, 2], [3, 1, -3], [1, 0, -2]]
b = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
x = gaussJordan(a, b)

print("Respuesta Caso 1")
for i in range(len(x)):
    for j in range(len(x[i])):
        print(round(x[i][j],6), end=' ')
    print()

print()    
print("Caso 2:")    

c = [[1, 2, 0, 4], [2, 0, -1, -2], [1, 1, -1, 0], [0,  4, 1, 0]]
d = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
y = gaussJordan(c, d)

print("Respuesta Caso 2")
for i in range(len(y)):
    for j in range(len(y[i])):
        print(round(y[i][j],6), end=' ')
    print()
