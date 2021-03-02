import matplotlib.pyplot as plt
import auxi.soluciones as sol
import numpy as np

t = sol.t
x = sol.x
y = sol.y

# SALIDA
np.set_printoptions(precision=6)
print(' [ ti, xi, yi]')
print(sol.estimacion)

plt.plot(sol.t, sol.x, label='xi presa')
plt.plot(sol.t , sol.y, label='yi predador')

plt.xlim(0, 30)
plt.ylim(0, 7)

plt.title('predador-presa')
plt.xlabel('t tiempo')
plt.legend()
plt.grid()
plt.show()

# gráfica xi vs yi
plt.plot(sol.x , sol.y)

plt.title('presa-predador')
plt.xlabel('presa')
plt.ylabel('depredador')
plt.grid()
plt.show()

'''plt.figure()
plt.title('Depredador - presa')

plt.xlabel('t')

t = sol.t
x = sol.x
y = sol.y

plt.plot(x, '-', lw=3, label='presa')
plt.plot(y, '-', lw=3, label='depredador')

plt.xlim(0, 30)
plt.ylim(0, 7)
plt.legend(loc='best')
plt.grid(True)

plt.savefig("grafico_item_b.jpg")
plt.show()
'''