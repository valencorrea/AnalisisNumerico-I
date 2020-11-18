import numpy as np

def estimar_ordenar_convergencia(raices, iteraciones):
    alfa = [0, 0, 0]
    ultimo_alfa = 0

    for n in range (3, iteraciones):
        xn_mas_uno = raices[n] - raices[n - 1]
        xn = raices[n - 1] - raices[n - 2]
        xn_menos_uno = raices[n - 2] - raices[n - 3]

        if xn_menos_uno == 0 or np.log10(np.abs(xn / xn_menos_uno)) == 0 or xn == 0:
            alfa[n] = n, np.inf
        else:
            ultimo_alfa = np.log10(np.abs(xn_mas_uno / xn)) / np.log10(np.abs(xn / xn_menos_uno))
            alfa.append(ultimo_alfa)

    alfa[0], alfa[1], alfa[2] = alfa[3], alfa[3], alfa[3] #para no usar el 0 como alfa

    return alfa