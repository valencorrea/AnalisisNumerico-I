import numpy as np

def estimar_ordenar_convergencia(raices, iteraciones):
    alfa = [0] * iteraciones

    for n in range (3, iteraciones):
        xn_mas_uno = raices[n] - raices[n - 1]
        xn = raices[n - 1] - raices[n - 2]
        xn_menos_uno = raices[n - 2] - raices[n - 3]

        if xn_menos_uno == 0 or np.log10(np.abs(xn / xn_menos_uno)) == 0 or xn == 0:
            return alfa
        else:
            ultimo_alfa = (np.log(np.abs(xn_mas_uno / xn))) / (np.log(np.abs(xn / xn_menos_uno)))
            alfa[n] = (ultimo_alfa)

    return alfa