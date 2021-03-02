from item_a.resultados import resultados
import matplotlib.pyplot as plt

t = resultados[:, 0]
x = resultados[:, 1]
y = resultados[:, 2]

plt.plot(x, y)

plt.title('depredador-presa')
plt.xlabel('presa')
plt.ylabel('depredador')
plt.legend(loc='best')
plt.grid(True)
plt.savefig("grafico_item_e.jpg")
plt.show()