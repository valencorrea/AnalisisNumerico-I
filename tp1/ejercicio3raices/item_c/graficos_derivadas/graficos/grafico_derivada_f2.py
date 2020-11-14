import matplotlib.pyplot as plt
import numpy as np
from item_c.graficos_derivadas.derivadas import derivada_f2 as df2

plt.figure()

cantidad_muestras = 50

# el rango de interes es desde 0 (no hay radios negativos) hasta 2R
inicio_rango = 0
fin_rango = 8.5

x2 = np.linspace(inicio_rango, fin_rango, cantidad_muestras)
y2 = df2.derivada_f2(x2)

plt.plot(x2, y2)

nombre_grafico = 'funcion 2 derivada'
plt.title(nombre_grafico)

plt.xlabel('x')
plt.ylabel('y')

plt.show()