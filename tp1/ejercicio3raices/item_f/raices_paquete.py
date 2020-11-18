import scipy.optimize as sc

import tp1.ejercicio3raices.item_a.f1_volumen_tanque as archivo_f1
import tp1.ejercicio3raices.item_b.f2_volumen_al_100 as archivo_f2

print(sc.brentq(archivo_f1.f1, 0, 2*4.25, xtol=1e-13, maxiter=12))
print(sc.brentq(archivo_f2.f2, 0, 2*4.25, xtol=1e-13, maxiter=12))
