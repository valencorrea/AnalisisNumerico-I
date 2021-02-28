import matplotlib.pyplot as plt
import item_a.soluciones as sol

#NO FUNCIONA XD

plt.figure()

maximo_vertical = 50
maximo_horizontal = 30

nombre_grafico = 'Depredador - presa (t)'
plt.title(nombre_grafico)

plt.xlabel('t')
plt.ylabel('x e y')

x = sol.solucion_x
y = sol.solucion_y
t = sol.tiempo

plt.plot(t, x)
plt.plot(t, y)
plt.show()

plt.savefig("grafico_item_b")
