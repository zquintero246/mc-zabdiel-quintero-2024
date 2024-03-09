
import math
x= float(input("Inserte Angulo en radianes"))



SenoX=math.sin(x)

es= (9.5*10**-8 * 100)

ea= 100
n = 3
Valor = x

iteracion = 1


signo = -1
while ea > es:
    Valor_ant = Valor

    Valor +=signo * (x**n)/math.factorial(n)
    ea = abs(Valor - Valor_ant) * 100
    iteracion +=1

    n += 2

    signo *= -1 

print("Respuesta",Valor)
print("ea:" + str(ea) + '%')
print('interaciones:',iteracion)

