import matplotlib.pyplot as plt
import numpy as np
from ejercicio3raices.item_c.graficos_derivadas.derivadas import derivada_f1 as df1

plt.figure()

cantidad_muestras = 50

# el rango de interes es desde 0 (no hay radios negativos) hasta 2R
inicio_rango = 0
fin_rango = 8.5

x1 = np.linspace(inicio_rango, fin_rango, cantidad_muestras)
y1 = df1.derivada_f1(x1)

plt.plot(x1,y1)

nombre_grafico = 'funcion 1 derivada'
plt.title(nombre_grafico)

plt.xlabel('x')
plt.ylabel('y')


plt.savefig("derivada_f1")
