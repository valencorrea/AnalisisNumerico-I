from runge_kutta import runge_kutta_orden4 as runge
from item_a.funciones import derivada_x
from item_a.funciones import derivada_y

# 30 0 300???
print("\nIngrese el número de presas, x = ")
x = (int)(input())
print("\nIngrese el número de depredadores, y = ")
y = (int)(input())

resultados = runge(derivada_x, derivada_y, 0, x, y, 0.1, 200)

print(resultados)