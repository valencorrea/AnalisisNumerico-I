import math
import numpy as np

def raices(a, b, c):
    
    if(a == 0):
    
        raise TypeError ("No se ingreso un polinomio de grado 2")
    
    elif b ** 2 < 4 * a * c:
        raise TypeError ("No se pueden calcular raices negativas")

    x1 = ( -b + math.sqrt( (b**2) - 4*a*c ) ) / (2*a)
    x2 = ( -b - math.sqrt( (b**2) - 4*a*c ) ) / (2*a)

    x1 = np.round(x1, 7) 
    x2 = np.round(x2, 7)
    return [x1, x2]



