import sys
import raices_optimizadas as ro
import matplotlib.pyplot as plt
import numpy as np


print(ro.raices_optimizadas(1, 10000000000000, 1))

print(ro.raices_optimizadas(1,2,1))

print(ro.raices_optimizadas(1000, 10000000, 1))

print(ro.raices_optimizadas(1, 1000000000000000, 0.00001))

print(ro.raices_optimizadas(1000, 100000000000, 1))

print(ro.raices_optimizadas(1000, 10000000000, 1))

print(ro.raices_optimizadas(1000, 10000000, 1))

print(ro.raices_optimizadas(0.000000000000001, 10000000010, 10))

try:
    
    ro.raices_optimizadas(0, 10000000010, 10)
    
except:
    
    print(sys.exc_info()[1]) # no se ingreso un polinomio de grado 2 

try:
    
    ro.raices_optimizadas(1, 0, 10)
    
except:
    
    print(sys.exc_info()[1]) # no se pueden calcular raices negativas


