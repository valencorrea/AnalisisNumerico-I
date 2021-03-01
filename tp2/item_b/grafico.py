import matplotlib.pyplot as plt
import item_a.soluciones as sol

plt.figure()
plt.title('Depredador - presa')

plt.xlabel('t')

x = sol.solucion_x[1]
t = sol.solucion_x[0]

plt.plot(x, '-', lw=3, label='presa')
plt.xlim(0, 50)
plt.ylim(0, 30)
plt.legend(loc='best')
plt.grid(True)

plt.savefig("grafico_item_b.jpg")
plt.show()
