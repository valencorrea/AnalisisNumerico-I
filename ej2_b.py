import math
import numpy as np

def raices(a, b, c):
    x1 = ( -b + math.sqrt( (b**2) - 4*a*c ) ) / (2*a)
    x2 = ( -b - math.sqrt( (b**2) - 4*a*c ) ) / (2*a)

    x1 = np.round(x1, 7)
    x2 = np.round(x2, 7)
    return [x1, x2]


def raiz(b, c):
    if b == 0:
        return [0]

    x = np.round(-c / b, 7)
    return [x]

def tiende_a_b(a, b, c):
    return [0, np.round(-b/a, 7)]

def raices_optimizadas(a, b, c):
    if b ** 2 < 4 * a * c:
        raise TypeError ("No se pueden calcular raices negativas")

    if a == 0:
        return raiz(b, c)

    elif (np.abs( -b - math.sqrt( (b**2) - 4*a*c ) ) - 2*a) > 1e9:
        return [4294967296]

    elif (2 * a - np.abs(-b - math.sqrt((b ** 2) - 4 * a * c))) > 1e9:
        return [0]

    elif (b**2 - 4*a*c) > 1e9:
        return tiende_a_b(a, b, c)

    return raices(a, b, c)

print(raices_optimizadas(1, 10000, 1))
print(raices_optimizadas(1,2,1))
print(raices_optimizadas(1000, 10000000, 1))
print(raices_optimizadas(1, 1000000000000000, 0.00001))
print(raices_optimizadas(1000, 100000000000, 1))
print(raices_optimizadas(1000, 10000000000, 1))
print(raices_optimizadas(1000, 10000000, 1))
print(raices_optimizadas(0.000000000000001, 10000000010, 10))

try:
    raices_optimizadas(1, 0, 10)
except:
    print("No se pueden calcular raices negativas")


