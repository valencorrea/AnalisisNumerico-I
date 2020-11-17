import numpy as np

def estimar_ordenar_convergencia(raices, iteraciones):
    alfa = [0]

    for n in range (2, iteraciones - 1):
        xn_mas_uno = raices[n + 1] - raices[n]
        xn = raices[n] - raices[n - 1]
        xn_menos_uno = raices[n - 1] - raices[n - 2]

        if xn_menos_uno == 0 or np.log10(np.abs(xn / xn_menos_uno)) == 0 or xn == 0:
            alfa[n] = n, np.inf
        else:
            alfa.append(np.log10( np.abs( xn_mas_uno / xn ) ) / np.log10(np.abs(xn / xn_menos_uno)))

    return alfa