import item_a.derivadas.funciones as f
from auxi.rungeKuttaOrden4 import runge_kutta as runge

estimacion = runge(f.derivada_x, f.derivada_y, 2, 1, 0.1, 0, 30)

t = estimacion[0]
x = estimacion[1]
y = estimacion[2]

print(t)
print(x)
print(y)


