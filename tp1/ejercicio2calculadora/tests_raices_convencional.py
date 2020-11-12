import sys
import raices_convencional as rc
import matplotlib.pyplot as plt
import numpy as np


print(rc.raices(1, 10000000000000, 1))

print(rc.raices(1,2,1))

print(rc.raices(1000, 10000000, 1))

print(rc.raices(1, 1000000000000000, 0.00001))

print(rc.raices(1000, 100000000000, 1))

print(rc.raices(1000, 10000000000, 1))

print(rc.raices(1000, 10000000, 1))

print(rc.raices(0.000000000000001, 10000000010, 10))

try:
    
    rc.raices(0, 10000000010, 10)
    
except:
    
    print(sys.exc_info()[1]) # no se ingreso un polinomio de grado 2 

try:
    
    rc.raices(1, 0, 10)
    
except:
    
    print(sys.exc_info()[1]) # no se pueden calcular raices negativas
    
    
    
#falta hacer el grafico
    
'''    
fig, axs =plt.subplots(2,1)

clust_data = np.random.random((10,3))

collabel=(" ", "raiz 1", "raiz 2")

axs[0].axis('tight')
axs[0].axis('off')

the_table = axs[0].table(cellText=pruebas,colLabels=collabel,loc='center')

contador = 123
axs[1].plot(contador, pruebas[:,0], pruebas[:,1])

plt.show()
'''
