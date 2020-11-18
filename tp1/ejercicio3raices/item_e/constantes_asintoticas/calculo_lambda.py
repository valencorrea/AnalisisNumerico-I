import numpy as np


def calcular_lambda(alfa, raices):
    constante_lambda = [0, 0]

    ultimo_lambda = 0


    for i in range(2, len(raices) - 1):

        xk = raices[i-1]
        xk_menos_uno = raices[i-2]
        xk_mas_uno = raices[i]

        ultimo_lambda = np.abs(xk_mas_uno - xk) / (np.abs(xk - xk_menos_uno)**alfa[i - 2])

        constante_lambda.append(ultimo_lambda)

    constante_lambda.append(ultimo_lambda)
    return constante_lambda
