from math import sqrt
import copy
import matplotlib.pyplot as plt
x=[1,3,5,7,9,11,13]
y=[7.4,1.8,-1,-1.8,-1.2,2.2,7.2]
n=len(x)
plt.plot(x, y, 'ro')
plt.show()

highx2 = []
highx3 = []
highx4 = []
multxy = []
highx2multx = []
for i in range(n):
    highx2.append(x[i]**2)
    highx3.append(x[i]**3)
    highx4.append(x[i]**4)
    multxy.append(x[i]*y[i])
    highx2multx.append((x[i]**2)*y[i])


sumatoria_x=sum(x)
sumatoria_y=sum(y)
sumatoria_highx2=sum(highx2)
sumatoria_highx3=sum(highx3)
sumatoria_highx4=sum(highx4)
sumatoria_multxy=sum(multxy)
sumatoria_highx2multx=sum(highx2multx)
promedio_y=sumatoria_y/n


a = [[n, sumatoria_x, sumatoria_highx2], [sumatoria_x, sumatoria_highx2, sumatoria_highx3], [sumatoria_highx2, sumatoria_highx3, sumatoria_highx4]]
b = [sumatoria_y, sumatoria_multxy, sumatoria_highx2multx]
matrizGauss = gaussJordan(a, b)



a0=matrizGauss[0]
a1=matrizGauss[1]
a2=matrizGauss[2]
print("a0: " + str(a0))
print("a1: " + str(a1))
print("a2: " + str(a2))


print("y: " + str(a0) + " + " + str(a1) + "x + " + str(a2) + "x^2")


stArray = []
srArray = []
for i in range(n):
    stArray.append((y[i]-promedio_y)**2)
    srArray.append((y[i]-a0-a1*x[i]-a2*x[i]**2)**2)


st=sum(stArray)
sr=sum(srArray)
print("St: " + str(st))
print("Sr: " + str(sr))



coef = sqrt((st-sr)/st)*100
print("Coef. Correlación: " + str(coef))



ry=[]
for i in range(n):
    ry.append(a0 + (a1*x[i]) + (a2*x[i]**2))




plt.plot(x, y, 'r--', x, ry, 'bs')
plt.show()



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
