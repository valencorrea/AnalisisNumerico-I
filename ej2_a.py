import math
import numpy as np

def raices(a, b, c):
    if b ** 2 < 4 * a * c:
        raise TypeError ("No se pueden calcular raices negativas")

    x1 = ( -b + math.sqrt( (b**2) - 4*a*c ) ) / (2*a)
    x2 = ( -b - math.sqrt( (b**2) - 4*a*c ) ) / (2*a)

    x1 = np.round(x1, 7)
    x2 = np.round(x2, 7)
    return [x1, x2]

print(raices(1, 10000, 1))
print(raices(1,2,1))
print(raices(1000, 10000000, 1))
print(raices(1, 1000000000000000, 0.00001))
print(raices(1000, 100000000000, 1))
print(raices(1000, 10000000000, 1))
print(raices(1000, 10000000, 1))
print(raices(0.000000000000001, 10000000010, 10))

try:
    raices_optimizadas(1, 0, 10)
except:
    print("No se pueden calcular raices negativas")