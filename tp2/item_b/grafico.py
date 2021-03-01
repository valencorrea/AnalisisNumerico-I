import matplotlib.pyplot as plt
import item_a.soluciones as sol

plt.figure()
plt.title('Depredador - presa')

plt.xlabel('t')

t = sol.solucion_x[0]
x = sol.solucion_x[1]
y = sol.solucion_y[1]

plt.plot(x, '-', lw=3, label='presa')
plt.plot(y, '-', lw=3, label='depredador')

plt.xlim(0, 30)
plt.ylim(0, 10)
plt.legend(loc='best')
plt.grid(True)

plt.savefig("grafico_item_b.jpg")
plt.show()
