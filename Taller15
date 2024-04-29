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
    b = copy.copy(bo)

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
        #Dividir por el pivote
        for j in range(n):
            a[i][j] /= pivote
        b[i] /= pivote
        imprimirSistema(a, b, "División")


        for k in range(n):
            if i != k:
                #Se reduce
                valorAux = -a[k][i]
                for j in range(n):
                    a[k][j] += a[i][j] * valorAux
                b[k] += b[i] * valorAux
        imprimirSistema(a, b, "Reducción")
    
    return b

a = [[1, 1, 0], [3, 3, 4], [4, 1, 0]]
b = [2.5, 11.5, 15]
x = gaussJordan(a, b)

print("Respuesta:")
for i in range(len(x)):
    print("x" + str(i+1), "=", x[i])

#Pruebas
print("\nPruebas:")
for i in range(len(b)):
    valorAux = b[i]
    for j in range(len(b)):
        valorAux -= a[i][j] * x[j]
    print("Test", i + 1, "=", valorAux)
