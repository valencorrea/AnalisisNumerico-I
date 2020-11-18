import tp1.ejercicio3raices.analisis_problema_fisico as analisis
import numpy as np
def f1(x):
    # Quiero ver el volumen a partir de 2R y el porcentaje pedido
    return analisis.v(x) - (analisis.v(2 * 4.25) * 0.5438596491)
def g1(x):
    return np.sqrt((analisis.v(2 * 4.25) * 0.5438596491 * 3 )/((3 * 4.25 - x) * np.pi))
