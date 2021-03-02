import matplotlib.pyplot as plt
import item_a.soluciones as sol

plt.figure()
plt.title('Depredador - presa')

plt.xlabel('t')

t = sol.t
x = sol.x
y = sol.y

plt.plot(x, '-', lw=3, label='presa')
plt.plot(y, '-', lw=3, label='depredador')

plt.xlim(0, 30)
plt.ylim(0, 10)
plt.legend(loc='best')
plt.grid(True)

plt.savefig("grafico_item_b.jpg")
plt.show()
