import numpy as np

#p es a lo que tiende la sucesión
def calcular_lambda(alfa, raices):
    constante_lambda = [0, 0]
    #k = len(raices) - 1
    ultimo_lambda = 0

    #le resto dos ya que no quiero que p == xn_mas_uno
    for i in range(2, len(raices) - 1):
        #x = raices[i]
        #ultimo_lambda = np.abs((x ** (k + 1)) - (x ** k)) / ((np.abs((x ** k) - x ** (k - 1))) ** alfa[i])

        xk = raices[i-1]
        xk_menos_uno = raices[i-2]
        xk_mas_uno = raices[i]

        ultimo_lambda = np.abs(xk_mas_uno - xk) / (np.abs(xk - xk_menos_uno)**alfa[i - 2])

        constante_lambda.append(ultimo_lambda)

    constante_lambda.append(ultimo_lambda)
    return constante_lambda
