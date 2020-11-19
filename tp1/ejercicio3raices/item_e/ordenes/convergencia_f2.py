import tp1.ejercicio3raices.item_e.ordenes.orden_convergencia as orden
from tp1.ejercicio3raices.item_d.resolucion_raices.raices_f2 import biseccion2
from tp1.ejercicio3raices.item_d.resolucion_raices.raices_f2 import nr2
from tp1.ejercicio3raices.item_d.resolucion_raices.raices_f2 import secante2
from tp1.ejercicio3raices.item_d.resolucion_raices.raices_f2 import nr_modificado2
from tp1.ejercicio3raices.item_d.resolucion_raices.raices_f2 import pfijo2
import matplotlib.pyplot as plt
import numpy as np

ordenb2 = orden.estimar_ordenar_convergencia(biseccion2[0], len(biseccion2[0]))
orden_nr2 = orden.estimar_ordenar_convergencia(nr2[0], len(nr2[0]))
orden_pf2 = orden.estimar_ordenar_convergencia(pfijo2[0], len(pfijo2[0]))
orden_secante2 = orden.estimar_ordenar_convergencia(secante2[0], len(secante2[0]))
orden_nr_modificado2 = orden.estimar_ordenar_convergencia(nr_modificado2[0], len(nr_modificado2[0]))

plt.figure()

x1 = np.linspace(0, len(biseccion2[0]), len(biseccion2[0]))
y1 = ordenb2[0:len(biseccion2[0])]

x2 = np.linspace(0, len(nr2[0])-4, len(nr2[0])-4)
y2 = orden_nr2[0:len(nr2[0])-4]

x3 = np.linspace(0, len(secante2[0]), len(secante2[0]))
y3 = orden_secante2[0:len(secante2[0])]

x4 = np.linspace(0, len(nr_modificado2[0]), len(nr_modificado2[0]))
y4 = orden_nr_modificado2[0:len(nr_modificado2[0])]

x5 = np.linspace(0, len(pfijo2[0]) - 4, len(pfijo2[0]) - 4)
y5 = orden_pf2[0:len(pfijo2[0]) - 4]


plt.plot(x1, y1, '-', lw=2, label='Biseccion')
plt.plot(x5, y5, '-', lw=2, label='Punto-fijo')
plt.plot(x2, y2, '-', lw=2, label='Newton-Raphson')
plt.plot(x4, y4, '-', lw=2, label='Newton-Raphson modificado')
plt.plot(x3, y3, '-', lw=2, label='Secante')

nombre_grafico = 'Orden de convergencia p para f2'
plt.title(nombre_grafico)

plt.xlabel('x')
plt.ylabel('Orden de convergencia p')
plt.legend(loc='best')
plt.grid(True)

plt.savefig("convergencia2.png")

plt.show()
