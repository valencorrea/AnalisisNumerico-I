import matplotlib.pyplot as plt
import numpy as np
from ejercicio3raices.item_b import f2_volumen_al_100 as vol


plt.figure()

cantidad_muestras = 50

# el rango de interes es desde 0 (no hay radios negativos) hasta 2R
inicio_rango = 0
fin_rango = 8.5

x2 = np.linspace(inicio_rango, fin_rango, cantidad_muestras)
y2 = vol.f2(x2)

plt.plot(x2, y2)

nombre_grafico = 'funcion 2'
plt.title(nombre_grafico)

plt.xlabel('radio')
plt.ylabel('altura(radio)')


plt.savefig("f2")
