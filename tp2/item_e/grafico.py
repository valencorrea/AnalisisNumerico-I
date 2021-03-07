from item_a.resultados import resultados
import matplotlib.pyplot as plt
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)

t = resultados[:, 0]
x = resultados[:, 1]
y = resultados[:, 2]
fig, ax = plt.subplots(figsize=(10, 8))

ax.set_xlim(0, 6)
ax.set_ylim(0, 4)

ax.xaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.set_major_locator(MultipleLocator(1))

ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))

ax.grid(which='major', color='#CCCCCC', linestyle='--')
ax.grid(which='minor', color='#CCCCCC', linestyle=':')
plt.plot(x, y)
plt.plot(1.6/0.6, 2.4/1.2, marker='o')
plt.title('depredador-presa')
plt.xlabel('presa')
plt.ylabel('depredador')
plt.savefig("grafico_item_e.jpg")
plt.show()
