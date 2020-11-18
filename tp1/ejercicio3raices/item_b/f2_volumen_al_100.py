import tp1.ejercicio3raices.analisis_problema_fisico as analisis
import numpy as np
def f2(x):
    # Quiero ver el volumen en 2R cuando el tanque se encuentra lleno al 100%
    return analisis.v(x) - (analisis.v(2 * 4.25) * 1)
def g2(x):
    return np.sqrt((analisis.v(2 * 4.25) * 1 * 3 )/((3 * 4.25 - x) * np.pi))
