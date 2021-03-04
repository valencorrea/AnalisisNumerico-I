import numpy as np

from item_a.resultados import resultados
import matplotlib.pyplot as plt
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)

t = resultados[:, 0]
x = resultados[:, 1]
y = resultados[:, 2]
fig, ax = plt.subplots(figsize=(10, 8))

ax.set_xlim(0, 30)
ax.set_ylim(0, 7)

ax.xaxis.set_major_locator(MultipleLocator(2))
ax.yaxis.set_major_locator(MultipleLocator(1))

ax.xaxis.set_minor_locator(AutoMinorLocator(2))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))

ax.grid(which='major', color='#CCCCCC', linestyle='--')
ax.grid(which='minor', color='#CCCCCC', linestyle=':')
plt.plot(t, x, label='presa')
plt.plot(t, y, label='depredador')
plt.savefig("grafico_item_b.jpg")
plt.show()