import numpy as np

def raiz(f, x0, tolerancia, iteraciones):
    xn = x0
    deltax = tolerancia + 1
    i = 0
    raices = []
    cotas = []

    while (deltax > tolerancia) and (i < iteraciones):
        i+=1
        temp = xn
        xn = g(f,temp)
        deltax = np.abs(g(f,xn) - g(f,temp))
        raices.append(xn)
        cotas.append(deltax)

    return raices, cotas

def g(f,x):
    return x-f(x)
