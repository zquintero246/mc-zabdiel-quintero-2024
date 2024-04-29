import math

x = 0.5
h = 0.005
signo = +1
valorAnt = 0
ea = 0

for i in range(15):
    if(i==0):
        valor = signo*(math.e)**-x
    else:
        valor = valorAnt + ((signo*(math.e)**-x/math.factorial(i))*(h**float(i)))
    print("orden " + str(i+1) + ": " + str(valor)) 
    ea = abs((valor-valorAnt)/valor)*100
    print("Error relativo: " + str(ea) + "%")
    valorAnt = valor
    signo = signo * -1
