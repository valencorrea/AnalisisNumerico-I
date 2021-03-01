import item_a.derivadas.funciones as f
from item_a.rungeKuttaOrden4 import runge_kutta as runge

solucion_x = runge(f.derivada_x, 2, 0.1, 0, 30)
#solucion_y = runge(f.derivada_y, 1, 0.1, 0, 30)

print(solucion_x)
#print(solucion_y)

