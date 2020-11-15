import scipy.optimize as sc

from ejercicio3raices.item_a import f1_volumen_tanque as archivo_f1
from ejercicio3raices.item_b import f2_volumen_al_100 as archivo_f2

print(sc.brentq(archivo_f1.f1, 0, 2*4.25, xtol=1e-13, maxiter=12))
print(sc.brentq(archivo_f2.f2, 0, 2*4.25, xtol=1e-13, maxiter=12))
