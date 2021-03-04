from runge_kutta import runge_kutta_orden4 as runge
from funciones import derivada_x
from funciones import derivada_y

# 30 0 300???
print("\nIngrese el parámetro a:")
a = (float)(input())
print("\nIngrese el parámetro b:")
b = (float)(input())
print("Ingrese el parámetro c:")
c = (float)(input())
print("Ingrese el parámetro d:")
d = (float)(input())

resultados = runge(derivada_x, derivada_y, 0, 2, 1, 0.1, 300, a, b, c, d)

print(resultados)