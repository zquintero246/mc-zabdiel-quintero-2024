from math import sqrt
x=[1,2,3,4,5,6,7]
y=[0.1,0.3,0.9,1.7,2.8,4.5,6.9]
n=len(x)

multxy = []
highx = []
for i in range(n):
    multxy.append(x[i]*y[i])
    highx.append(x[i]**2)
  
sumatoria_x=sum(x)
sumatoria_y=sum(y)
sumatoria_multxy=sum(multxy)
sumatoria_highx=sum(highx)
promedio_x=sumatoria_x/n
promedio_y=sumatoria_y/n
a1=((n*sumatoria_multxy)-(sumatoria_x*sumatoria_y))/((n*sumatoria_highx-sumatoria_x**2))
a0=promedio_y-(a1*promedio_x)
print("y = " + str(a0) + " + " + str(a1) + "x")

starray = []
srarray = []
for i in range(n):
    starray.append((y[i]-promedio_y)**2)
    srarray.append((y[i]-a0-(a1*x[i]))**2)


st=sum(starray)
sr=sum(srarray)
print("St: " + str(st))
print("Sr: " + str(sr))

sy = sqrt(st/(n-1))
errorEstandar = sqrt(sr/(n-2))
print("Desviación Estándar: " + str(sy))
print("Error Estándar: " + str(errorEstandar))

coeDet = (st-sr)/st
coeCorre = sqrt(coeDet)*100
print("Coef. Determinación: " + str(coeDet))
print("Coef. Correlación: " + str(coeCorre) + "%")
