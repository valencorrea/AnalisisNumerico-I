import numpy as np

def calcular_lambda(alfa, pn_mas_uno, pn):
    if np.abs(pn)**alfa == 0:
        return 0

    return np.abs(pn_mas_uno) / np.abs(pn)**alfa