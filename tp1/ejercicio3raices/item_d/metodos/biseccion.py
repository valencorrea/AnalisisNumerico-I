import numpy as np

def seleccion_p(f, a, b):
    p = (b + a) / 2

    if f(a) * f(p) > 0:
        return p, p, b
    else:
        return p, a, p

def raiz(f, a, b, tolerancia, iteraciones):
    if f(a) * f(b) > 0:
        return ["Error, f(a).f(b) > 0"]
    i = 0

    p, a, b = seleccion_p(f, a, b)
    deltax = tolerancia + 1

    raices = []
    cotas = []

    while (i < iteraciones) and (np.abs(deltax) > tolerancia):
        i += 1
        deltax = np.abs(f(p) - f((b + a) / 2))
        p, a, b = seleccion_p(f, a, b)
        raices.append(p)
        cotas.append(deltax)

    return raices, cotas