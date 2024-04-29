import math
from math import e
import numpy as np
import matplotlib.pyplot as plt
#Variables
x=[1,2,3,4,5,6,7,8]
y=[4.3,6.5,7.5,8,8.5,8.8,9,9.5]
n=len(x)


plt.plot(x, y, 'ro')
plt.show()


multxyReg1 = []
highxReg1 = []

lnyReg2=[]
multxlnyReg2=[]
highxReg2 = []

lnxPot=[]
lnyPot=[]
multlnxlnyPot=[]
highlnxPot = []

divxRaz=[]
divyRaz=[]
multdivxdivyRaz=[]
highdivxRaz=[]
for i in range(n):

  multxyReg1.append(x[i]*y[i])
  highxReg1.append(x[i]**2)

  lnyReg2.append(np.log(y[i]))
  multxlnyReg2.append(x[i]*lnyReg2[i])
  highxReg2.append(x[i]**2)
  
  lnxPot.append(math.log10(x[i]))
  lnyPot.append(math.log10(y[i]))
  multlnxlnyPot.append(lnxPot[i]*lnyPot[i])
  highlnxPot.append(lnxPot[i]**2)
  
  divxRaz.append(1/x[i])
  divyRaz.append(1/y[i])
  multdivxdivyRaz.append(divxRaz[i]*divyRaz[i])
  highdivxRaz.append(divxRaz[i]**2)
