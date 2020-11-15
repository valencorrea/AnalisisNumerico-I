import scipy.optimize as sc

from ejercicio3raices.item_a import f1_volumen_tanque as f1
from ejercicio3raices.item_b import f2_volumen_al_100 as f2

print(sc.brentq(f1, 0, 2*4.25, xtol=1e-13, maxiter=12))
print(sc.brentq(f2, 0, 2*4.25, xtol=1e-13, maxiter=12))
