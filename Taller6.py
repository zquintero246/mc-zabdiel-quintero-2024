from decimal import Decimal, getcontext
import math

# Set precision for Decimal calculations
getcontext().prec = 50

x = Decimal(input("Por favor, ingrese el valor de un ángulo en radianes=\n-"))
Form = Decimal('0.5') * Decimal('1e-8') * Decimal('100')

a = Decimal('100')
varAct = Decimal('0')
iteraciones = 2

while a > Form:
    varAnt = varAct
    varAct = varAct + ((-1)**(iteraciones//2))*(x**iteraciones) / Decimal(math.factorial(iteraciones))
    a = abs((varAct - varAnt) / varAct) * Decimal('100')
    iteraciones += 2

print(f"El valor estimado es de: {varAct}")
print(f"El error aproximado relativo porcentual es de: {a}")
print(f"El número de iteraciones realizadas es de: {iteraciones//2}")
