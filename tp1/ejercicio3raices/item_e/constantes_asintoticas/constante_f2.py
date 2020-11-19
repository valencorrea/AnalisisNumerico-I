import tp1.ejercicio3raices.item_e.constantes_asintoticas.calculo_lambda as calc
import tp1.ejercicio3raices.item_d.resolucion_raices.raices_f2 as modos
import tp1.ejercicio3raices.item_e.ordenes.orden_convergencia as orden
import matplotlib.pyplot as plt
import numpy as np

ordenb2 = orden.estimar_ordenar_convergencia(modos.biseccion2[0], len(modos.biseccion2[0]))
orden_nr2 = orden.estimar_ordenar_convergencia(modos.nr2[0], len(modos.nr2[0]))
orden_pf2 = orden.estimar_ordenar_convergencia(modos.pfijo2[0],len(modos.pfijo2[0]))
orden_secante2 = orden.estimar_ordenar_convergencia(modos.secante2[0], len(modos.secante2[0]))
orden_nr_modificado2 = orden.estimar_ordenar_convergencia(modos.nr_modificado2[0], len(modos.nr_modificado2[0]))

lambda_b2 = calc.calcular_lambda(ordenb2, modos.biseccion2[0])
lambda_nr2 = calc.calcular_lambda(orden_nr2, modos.nr2[0])
lambda_pf2 = calc.calcular_lambda(orden_pf2, modos.pfijo2[0])
lambda_secante2 = calc.calcular_lambda(orden_secante2, modos.secante2[0])
lambda_nr_modificado2 = calc.calcular_lambda(orden_nr_modificado2, modos.nr_modificado2[0])

plt.figure()

# el rango de interes es desde 0 (no hay radios negativos) hasta 2R

x1 = np.linspace(0, len(modos.biseccion2[0]), len(modos.biseccion2[0]))
y1 = lambda_b2

x2 = np.linspace(0, len(modos.nr2[0]) - 2, len(modos.nr2[0]) - 2)
y2 = lambda_nr2[0:23]

x3 = np.linspace(0, len(modos.secante2[0]), len(modos.secante2[0]))
y3 = lambda_secante2[0]

x4 = np.linspace(0, len(modos.nr_modificado2[0]), len(modos.nr_modificado2[0]))
y4 = lambda_nr_modificado2
x5 = np.linspace(0, len(modos.pfijo2[0]) - 4, len(modos.pfijo2[0]) - 4)
y5 = lambda_pf2[0:len(modos.pfijo2[0]) - 4]

plt.plot(x1, y1, '-', lw=2, label='Biseccion')
plt.plot(x5, y5, '-', lw=2, label='Punto_fijo')
plt.plot(x2, y2, '-', lw=2, label='Newton-Raphson')
plt.plot(x4, y4, '-', lw=2, label='Newton-Raphson modificado')
plt.plot(x3, y3, '-', lw=2, label='Secante')

nombre_grafico = 'Constante asintótica f2'
plt.title(nombre_grafico)

plt.xlabel('x')
plt.ylabel('constante asintotica')
plt.legend(loc='best')
plt.grid(True)

plt.savefig("constante_f2.png")

plt.show()
