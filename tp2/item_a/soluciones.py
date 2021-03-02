import item_a.derivadas.funciones as f
from item_a.rungeKuttaOrden4 import runge_kutta as runge

t, x, y = runge(f.derivada_x, f.derivada_y, 2, 1, 0.5, 0, 101)

print(t)
print(x)
print(y)


