import item_a.derivadas.funciones as f
from item_a.rungeKuttaOrden4 import runge_kutta as runge

tupla_x = runge(f.derivada_x, 2, 1, 0.1, 0, 30)
tiempo = tupla_x[0]

solucion_x = tupla_x[1]
solucion_y = runge(f.derivada_y, 2, 1, 0.1, 0, 30)[1]

print(solucion_x)
print(solucion_y)
