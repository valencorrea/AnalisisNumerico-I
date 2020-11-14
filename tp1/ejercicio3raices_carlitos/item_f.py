import scipy.optimize as sc
import analisis_problema_fisico as analisis
from tp1.ejercicio2calculadora.modelo import raices_optimizadas as ro

import numpy as np

def f1(x):
    return analisis.v(x) - (analisis.v(2*4.25) * 0.5438596491)

def f2(x):
    return analisis.v(x) - analisis.v(2 * 4.25)

print(sc.brentq(f1, 0, 2*4.25, xtol=1e-13, maxiter=12))
print(sc.brentq(f2, 0, 2*4.25, xtol=1e-13, maxiter=12))

print(ro.raices_optimizadas(-np.pi, 2 * 12.75 * np.pi / 3, 0))