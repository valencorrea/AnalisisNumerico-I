import tp1.ejercicio3raices.item_e.constantes_asintoticas.calculo_lambda as calc
import tp1.ejercicio3raices.item_d.resolucion_raices.raices_f1 as modos
import tp1.ejercicio3raices.item_e.ordenes.convergencia_f1 as orden
import numpy as np
import matplotlib.pyplot as plt

lambda_b1 = calc.calcular_lambda(orden.ordenb1, modos.biseccion1[0])
lambda_nr1 = calc.calcular_lambda(orden.orden_nr1, modos.nr1[0])
lambda_secante1 = calc.calcular_lambda(orden.orden_secante1, modos.secante1[0])
lambda_nr_modificado1 = calc.calcular_lambda(orden.orden_nr_modificado1, modos.nr_modificado1[0])

plt.figure()

cantidad_muestras = 48

# el rango de interes es desde 0 (no hay radios negativos) hasta 2R
inicio_rango = 0
fin_rango = 46

x1 = np.linspace(inicio_rango, fin_rango, cantidad_muestras)
y1 = lambda_b1[0:48]

x2 = np.linspace(0, len(modos.nr1[0]), len(modos.nr1[0]))
y2 = lambda_nr1

x3 = np.linspace(0, len(modos.secante1[0]) - 3, len(modos.secante1[0]) - 3)
y3 = lambda_secante1[0:4]

x4 = np.linspace(0, len(modos.nr_modificado1[0]), len(modos.nr_modificado1[0]))
y4 = lambda_nr_modificado1


plt.plot(x1, y1, '-', lw=2, label='Biseccion')
plt.plot(x2, y2, '-', lw=2, label='Newton-Raphson')
plt.plot(x3, y3, '-', lw=2, label='Secante')
plt.plot(x4, y4, '-', lw=2, label='Newton-Raphson modificado')


nombre_grafico = 'Constante asintótica'
plt.title(nombre_grafico)

plt.xlabel('x')
plt.ylabel('constante asintotica')
plt.legend(loc='best')
plt.grid(True)


plt.savefig("biseccion1.png")
