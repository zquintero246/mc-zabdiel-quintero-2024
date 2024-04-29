x=[1,2,3,4,5,6,7,8]
y=[9,7,8,5,6,4.5,4,2.5]
multxy = []
highx = []
n=len(x)
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
