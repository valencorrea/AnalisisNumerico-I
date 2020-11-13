import sys
import raices_convencional as rc
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

p1 = rc.raices(1, 10000000000000, 1)

p2 = (rc.raices(1, 2, 1))

p3 = (rc.raices(1000, 10000000, 1))

p4 = (rc.raices(1, 1000000000000000, 0.00001))

p5 = (rc.raices(1000, 100000000000, 1))

p6 = (rc.raices(1000, 10000000000, 1))

p7 = (rc.raices(1000, 10000000, 1))

p8 = (rc.raices(0.000000000000001, 10000000010, 10))

p9 = (rc.raices(1, 1e32, 1))

try:

    rc.raices(0, 10000000010, 10)

except:

    print(sys.exc_info()[1])  # no se ingreso un polinomio de grado 2

try:

    rc.raices(1, 0, 10)

except:

    print(sys.exc_info()[1])  # no se pueden calcular raices negativas


data = {'a': [1, 1, 1000, 1, 1000, 1000, 1000, 0.000000000000001, 1],
        'b': [10000000000000, 2, 10000000, 1000000000000000, 100000000000, 10000000000, 10000000, 10000000010, 1e32],
        'c': [1, 1, 1, 0.00001, 1, 1, 1, 10, 1],
        'x1': [p1[0], p2[0], p3[0], p4[0], p5[0], p6[0], p7[0], p8[0], p9[0]],
        'x2': [p1[1], p2[1], p3[1], p4[1], p5[1], p6[1], p7[1], p8[1], p9[1]]}

df = pd.DataFrame(data, columns = ['a', 'b', 'c', 'x1', 'x2'])

df.to_csv('convencional.csv')

df = pd.read_csv('convencional.csv')

print(df)

# falta hacer el grafico

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