import numpy as np
import biseccion as bi


def raiz(f, derivada, a, b, tolerancia, iteraciones):
    biseccion = bi.raiz(f, a, b, tolerancia, 2)
    xns = biseccion[0]
    dxs = biseccion[1]
    xn = xns[len(xns) - 1]
    deltax = dxs[len(dxs) - 1]

    i = 0
    raices = [xn]
    cotas = [deltax]

    while (i < iteraciones) and (deltax > tolerancia):
        i+=1
        if derivada(xn) == 0:
            return raices, cotas

        temp = xn
        xn = xn - (f(xn) / derivada(xn))
        deltax = np.abs(f(xn) - f(temp))
        raices.append(xn)
        cotas.append(deltax)

    return raices, cotas