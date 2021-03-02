import matplotlib.pyplot as plt
from item_a.runge_kutta import runge_kutta_orden4
import numpy as np
from item_a.funciones import derivada_x
from item_a.funciones import derivada_y

# PROCEDIMIENTO
tabla = runge_kutta_orden4(derivada_x, derivada_y, 0, 2, 1, 0.1,300)
ti = tabla[:,0]
xi = tabla[:,1]
yi = tabla[:,2]

# SALIDA
np.set_printoptions(precision=6)
print(' [ ti, xi, yi]')
print(tabla)


plt.plot(ti,xi, label='xi presa')
plt.plot(ti,yi, label='yi predador')

plt.xlim(0, 30)
plt.ylim(0, 7)

plt.title('predador-presa')
plt.xlabel('t tiempo')
plt.legend()
plt.grid()
plt.show()

# gráfica xi vs yi
plt.plot(xi,yi)

plt.title('presa-predador')
plt.xlabel('presa')
plt.ylabel('depredador')
plt.grid()
plt.show()