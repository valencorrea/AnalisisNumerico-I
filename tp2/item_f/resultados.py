from runge_kutta import runge_kutta_orden4 as runge
from funciones import derivada_x
from funciones import derivada_y

x = 0.8/0.3
y = 1.2/0.6

resultados = runge(derivada_x, derivada_y, 0, x, y, 0.1, 200)

print(resultados)