import numpy as np
from tp1.ejercicio3raices.item_d.metodos import biseccion as bi

def raiz(f, derivada, derivada_segunda, a, b, tolerancia, iteraciones):
    biseccion = bi.raiz(f, a, b, tolerancia, 2)
    historial_raices = biseccion[0]
    historial_cotas = biseccion[1]
    xn = historial_raices[len(historial_raices) - 1]
    deltax = historial_cotas[len(historial_cotas) - 1]

    i = 0
    raices = []
    cotas = []

    while i < iteraciones and deltax > tolerancia:
        i+=1
        xn_old = xn
        xn = xn_old - ( (f(xn_old) * derivada(xn_old)) / ((derivada(xn_old) ** 2) - (f(xn_old) * derivada_segunda(xn_old))))
        deltax = np.abs(f(xn) - f(xn_old))
        raices.append(xn)
        cotas.append(deltax)

    return raices, cotas
