from math import e
import numpy as np
import matplotlib.pyplot as plt
x=[1,2,3,4,5,6]
y=[1.6,2.3,3.4,4.5,6.4,9]
lny=[]
multxlny=[]
highx = []
n=len(x)


plt.plot(x, y, 'ro')
plt.show()


for i in range(n):
    lny.append(np.log(y[i]))
    multxlny.append(x[i]*lny[i])
    highx.append(x[i]**2)

sumatoria_x=sum(x)
sumatoria_lny=sum(lny)
sumatoria_multxlny=sum(multxlny)
sumatoria_highx=sum(highx)


promedio_x=sumatoria_x/n
promedio_lny=sumatoria_lny/n


a1=((n*sumatoria_multxlny)-(sumatoria_x*sumatoria_lny))/((n*sumatoria_highx-sumatoria_x**2))
a0=promedio_lny-(a1*promedio_x)


alfa = e**a0
beta = a1
print("y = " + str(alfa) + "*e^" + str(beta) + "x")


ry=[]
for i in range(n):
    ry.append(alfa*(e**(beta*x[i])))

plt.plot(x, y, 'r--', x, ry, 'bs')
plt.show()
