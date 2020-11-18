import numpy as np

from tp1.ejercicio3raices.item_d.metodos import punto_fijo as pf, secante as se, newton_raphson as nr, newton_raphson_modificado as nrm, \
    biseccion as bi


def f1(x):
    return np.sin(x)

def derivada1(x):
    return np.cos(x)

def derivada_segunda1(x):
    return -np.sin(x)

print("BISECCION")

print(bi.raiz(f1, np.pi/2, 3*np.pi/2, 0.00001, 20))
print(bi.raiz(f1, 1, 4, 0.00001, 20))

print("-------------------------------------------------------------")

print("PUNTO FIJO")
print(pf.raiz(f1, np.pi/2, 0.00001, 20))
print(pf.raiz(f1, 1, 0.00001, 20))

print("-------------------------------------------------------------")

print("NEWTON-RAPHSON")
print(nr.raiz(f1, derivada1, np.pi/2, 3*np.pi/2, 0.00001, 20))
print(nr.raiz(f1, derivada1, 1, 4, 0.00001, 20))

print("-------------------------------------------------------------")

print("SECANTE")
print(se.raiz(f1, np.pi/2, 3*np.pi/2, 0.00001, 20))
print(se.raiz(f1, 1, 4, 0.00001, 20))

print("-------------------------------------------------------------")

print("NEWTON-RAPHSON MODIFICADO")
print(nrm.raiz(f1, derivada1, derivada_segunda1, np.pi/2, 3*np.pi/2, 0.00001, 20))
print(nrm.raiz(f1, derivada1, derivada_segunda1, 1, 4, 0.00001, 20))
