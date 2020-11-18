import math
import numpy as np

def raiz_1_equivalente(a, b, c):
    
    return  np.round( (-2 * c) / ( b + math.sqrt(b**2 - (4 * a * c) ) ), 7)


def raiz_2_convencional(a, b, c):
    
    return  np.round( ( ( -b - math.sqrt(b**2 - (4 * a * c) ) ) / (2 * a)), 7)
    

def raices_optimizadas(a, b, c):
    
    if(a == 0):
    
        raise TypeError ("No se ingreso un polinomio de grado 2")
    
    elif(b ** 2 < 4 * a * c):
        
        raise TypeError ("No se pueden calcular raices negativas")
    
    # contempla el caso de que (b^2 - 4ac) > 1e7
    return [raiz_1_equivalente(a, b, c), raiz_2_convencional(a, b, c)]





