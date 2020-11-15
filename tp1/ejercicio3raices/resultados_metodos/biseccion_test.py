import numpy as np
from ejercicio3raices.item_d import biseccion as bi


def funcion(x):

    return np.sin(x)

print()
print("Metodo: Biseccion")
print()

print("Prueba 1") #renombrar prueba
print()

raices_biseccion = bi.raiz(funcion, np.pi/2, 3*np.pi/2, 0.00001, 20)[0]
iteracion = 0

for raiz in raices_biseccion:
    print("Iteracion nº{0}: {1}".format(iteracion, raices_biseccion[iteracion]))
    iteracion += 1

print()
print()
print("Prueba 2") #renombrar prueba
print()

raices_biseccion = bi.raiz(funcion, 1, 4, 0.00001, 20)[0]
iteracion = 0

for raiz in raices_biseccion:
    print("Iteracion nº{0}: {1}".format(iteracion, raices_biseccion[iteracion]))
    iteracion += 1

