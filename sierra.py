# Realizado por santiago jimenez guerrero

from sympy import *
import numpy as np
from scipy import signal
from sympy.abc import t, n,x
import matplotlib.pyplot as plt

print("Serie de Fourier - sierra")
ao = integrate((x), (x, 0, 1))

print ("\n"+"a0 = ")
pprint(ao)

an =  together(integrate((x*cos(n*pi*x)), (x, 0, 1)) )

print ("\n"+"an = ")
pprint(an)

bn =  together(integrate((x*sin(n*pi*x)), (x, 0, 1)))

#grafica_onda

print ("\n"+"bn = ")
pprint(bn)


print ("\n"+"f(x) = ")

armonicos = 50

serie = (ao/2)
for i in range(1, armonicos + 1):
    serie = serie + (an*cos(n*x*pi)).subs(n, i)
for j in range(1, armonicos + 1):
    serie = serie + (bn*sin(n*x*pi)).subs(n, j)


pprint(serie)
plotting.plot(serie, ylim=(-4, 4), xlim=(-4,4)) #Usando el modulo para graficas de sympy


x = [-4,-3,-3.01,-2,-1,-1.01,0,1,1.01,2,3,3.01,4]
y = [0,1,0,0,1,0,0,1,0,0,1,0,0]

plt.plot(x,y,)
plt.xlim((-4, 4))
plt.ylim(-4,4)
plt.show()


