from runge_kutta import runge_kutta_orden4 as runge
from funciones import derivada_x
from funciones import derivada_y

x = 0
y = 0

resultados = runge(derivada_x, derivada_y, 0, x, y, 0.1, 200)

print(resultados)