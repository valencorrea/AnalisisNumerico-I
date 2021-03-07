from item_g.resultados import resultados
import matplotlib.pyplot as plt

t = resultados[:, 0]
x = resultados[:, 1]
y = resultados[:, 2]

plt.plot(x, y)
plt.plot(0.8/0.3, 1.2/0.6, marker='o')

plt.title('depredador-presa')
plt.xlabel('presa')
plt.ylabel('depredador')
#plt.legend(loc='best')
plt.grid(True)
plt.savefig("grafico_lissajous_item_f.jpg")
plt.show()