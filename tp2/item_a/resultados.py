from item_a.runge_kutta import runge_kutta_orden4 as runge
from item_a.funciones import derivada_x
from item_a.funciones import derivada_y

# 30 0 300???
resultados = runge(derivada_x, derivada_y, 0, 2, 1, 0.1, 300)

print(resultados)