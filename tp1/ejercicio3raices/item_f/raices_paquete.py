import scipy.optimize as sc

import tp1.ejercicio3raices.item_a.f1_volumen_tanque as f
import tp1.ejercicio3raices.item_b.f2_volumen_al_100 as fdos

print(sc.brentq(f.f1, 0, 2*4.25, xtol=1e-13, maxiter=12))
print(sc.brentq(fdos.f2, 0, 2*4.25, xtol=1e-13, maxiter=12))
