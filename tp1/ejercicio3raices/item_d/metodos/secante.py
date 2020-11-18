import numpy as np

def raiz(f, a, b, tolerancia, iteraciones):
    xn_0 = a
    xn_1 = b
    xn = 0
    deltax = tolerancia + 1
    i = 0
    raices = []
    cotas = []

    while i < iteraciones and deltax > tolerancia:
        i+=1
        xn = xn_1 - (f(xn_1) * (xn_1 - xn_0)) / (f(xn_1) - f(xn_0))
        xn_0 = xn_1
        xn_1 = xn

        deltax = np.abs(f(xn_1) - f(xn_0))
        raices.append(xn)
        cotas.append(deltax)

    return raices, cotas
