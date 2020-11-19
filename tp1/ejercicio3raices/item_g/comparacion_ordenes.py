import matplotlib.pyplot as plt
from tp1.ejercicio3raices.item_e.ordenes.convergencia_f1 import ordenb1
from tp1.ejercicio3raices.item_e.ordenes.convergencia_f1 import orden_nr1
from tp1.ejercicio3raices.item_e.ordenes.convergencia_f1 import orden_secante1
from tp1.ejercicio3raices.item_e.ordenes.convergencia_f1 import orden_nr_modificado1
from tp1.ejercicio3raices.item_e.ordenes.convergencia_f1 import orden_pf1

from tp1.ejercicio3raices.item_e.ordenes.convergencia_f2 import ordenb2
from tp1.ejercicio3raices.item_e.ordenes.convergencia_f2 import orden_nr2
from tp1.ejercicio3raices.item_e.ordenes.convergencia_f2 import orden_secante2
from tp1.ejercicio3raices.item_e.ordenes.convergencia_f2 import orden_nr_modificado2
from tp1.ejercicio3raices.item_e.ordenes.convergencia_f2 import orden_pf2

plt.figure()

plt.plot(ordenb1[:], '-', lw=2, label='Biseccion')
plt.plot(orden_pf1[:], '-', lw=2, label='Punto fijo')
plt.plot(orden_nr1[:], '-', lw=2, label='NR')
plt.plot(orden_nr_modificado1[:], '-', lw=2, label='Newton-Raphson modificado')
plt.plot(orden_secante1[:], '-', lw=2, label='Secante')

plt.title('Raices para f1(x)')

plt.xlabel('Paso [n]')
plt.ylabel('alfa')

plt.legend(loc='best')
plt.grid(True)
plt.savefig("raices_f1.jpg")

plt.show()

plt.figure()

plt.plot(ordenb2[:], '-', lw=2, label='Biseccion')
plt.plot(orden_pf2[0:len(orden_pf2) - 3], '-', lw=2, label='Punto fijo')
plt.plot(orden_nr2[0:len(orden_nr2) - 3], '-', lw=2, label='NR')
plt.plot(orden_nr_modificado2[:], '-', lw=2, label='Newton-Raphson modificado')
plt.plot(orden_secante2[:], '-', lw=2, label='Secante')

plt.title('Raices para f2(x)')

plt.xlabel('Paso [n]')
plt.ylabel('alfa')

plt.legend(loc='best')
plt.grid(True)
plt.savefig("raices_f2.jpg")

plt.show()
