import numpy as np


def raiz(g, x0, tolerancia, iteraciones):
    xn = x0
    deltax = tolerancia + 1
    i = 0
    raices = []
    cotas = []

    while (deltax > tolerancia) and (i < iteraciones):
        i+=1
        temp = xn
        xn = g(temp)
        deltax = np.abs(g(xn) - g(temp))
        raices.append(xn)
        cotas.append(deltax)

    return raices, cotas

