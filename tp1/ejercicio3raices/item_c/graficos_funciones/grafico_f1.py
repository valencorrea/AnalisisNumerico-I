import matplotlib.pyplot as plt
import numpy as np
from tp1.ejercicio3raices.item_a import f1_volumen_tanque as vol


plt.figure()

cantidad_muestras = 50

# el rango de interes es desde 0 (no hay radios negativos) hasta 2R
inicio_rango = 0
fin_rango = 8.5

x1 = np.linspace(inicio_rango, fin_rango, cantidad_muestras)
y1 = vol.f1(x1)

plt.plot(x1, y1)

nombre_grafico = 'funcion 1'
plt.title(nombre_grafico)

plt.xlabel('radio')
plt.ylabel('altura(radio)')


plt.savefig("f1")
