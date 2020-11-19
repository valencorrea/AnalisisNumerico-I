import tp1.ejercicio3raices.item_e.ordenes.orden_convergencia as orden
from tp1.ejercicio3raices.item_d.resolucion_raices.raices_f1 import biseccion1
from tp1.ejercicio3raices.item_d.resolucion_raices.raices_f1 import nr1
from tp1.ejercicio3raices.item_d.resolucion_raices.raices_f1 import secante1
from tp1.ejercicio3raices.item_d.resolucion_raices.raices_f1 import nr_modificado1
from tp1.ejercicio3raices.item_d.resolucion_raices.raices_f1 import pfijo1
import matplotlib.pyplot as plt
import numpy as np

ordenb1 = orden.estimar_ordenar_convergencia(biseccion1[0], len(biseccion1[0]))
orden_nr1 = orden.estimar_ordenar_convergencia(nr1[0], len(nr1[0]))
orden_pf1 = orden.estimar_ordenar_convergencia(pfijo1[0],len(pfijo1[0]))
orden_secante1 = orden.estimar_ordenar_convergencia(secante1[0], len(secante1[0]))
orden_nr_modificado1 = orden.estimar_ordenar_convergencia(nr_modificado1[0], len(nr_modificado1[0]))
plt.figure()

x1 = np.linspace(0, len(biseccion1[0]) - 5, len(biseccion1[0]) - 5)
y1 = ordenb1[0:len(biseccion1[0])-5]


x2 = np.linspace(0, len(nr1[0])-2, len(nr1[0])-2)
y2 = orden_nr1[0:len(nr1[0])-2]

x3 = np.linspace(0, len(secante1[0])-4, len(secante1[0])-4)
y3 = orden_secante1[0:len(secante1[0])-4]

x4 = nplt.show()
p.linspace(0, len(nr_modificado1[0])-2, len(nr_modificado1[0])-2)
y4 = orden_nr_modificado1[0:len(nr_modificado1[0])-2]

x5 = np.linspace(0, len(pfijo1[0]), len(pfijo1[0]))
y5 = orden_pf1[0:len(pfijo1[0])]


plt.plot(x1, y1, '-', lw=2, label='Biseccion')
plt.plot(x5, y5, '-', lw=2, label='Punto-fijo')
plt.plot(x2, y2, '-', lw=2, label='Newton-Raphson')
plt.plot(x4, y4, '-', lw=2, label='Newton-Raphson modificado')
plt.plot(x3, y3, '-', lw=2, label='Secante')

nombre_grafico = 'Orden de convergencia p para f1'
plt.title(nombre_grafico)

plt.xlabel('x')
plt.ylabel('Orden de convergencia p')
plt.legend(loc='best')
plt.grid(True)

plt.savefig("convergencia1.png")

plt.show()
