from item_a.resultados import resultados
import matplotlib.pyplot as plt

t = resultados[:, 0]
x = resultados[:, 1]
y = resultados[:, 2]

plt.plot(t, x, label='presa')
plt.plot(t, y, label='depredador')

plt.xlim(0, 30)
plt.ylim(0, 7)

plt.title('depredador-presa')
plt.xlabel('tiempo')
plt.legend()
plt.grid()
plt.show()