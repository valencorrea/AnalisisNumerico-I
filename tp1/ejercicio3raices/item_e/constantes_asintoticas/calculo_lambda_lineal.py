import numpy as np
import scipy.optimize as sc

#p es a lo que tiende la sucesión
def calcular_lambda(alfa, raices):
    constante_lambda = [0]

    xn = raices[len(raices) - 3]
    xn_mas_uno = raices[len(raices) - 3 + 1]
    xn_mas_dos = raices[len(raices) - 3 + 2]
    p = ((xn_mas_dos * xn) - (xn_mas_uno ** 2)) / (xn_mas_dos - 2 * xn_mas_uno + xn)

    #le resto dos ya que no quiero que p == xn_mas_uno
    for i in range(len(raices) - 2):
        xn = raices[i]
        xn_mas_uno = raices[i+1]

        if xn - p == 0:
            return constante_lambda

        al = alfa[len(alfa) - 2]
        a = np.abs( xn_mas_uno - p )
        b = np.abs(( xn - p ))**(al)

        constante_lambda.append( a / b )

    return constante_lambda

