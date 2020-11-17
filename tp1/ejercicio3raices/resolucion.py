import tp1.analisis_problema_fisico as analisis

from tp1.ejercicio3raices.item_d.metodos import secante as se, newton_raphson as nr, newton_raphson_modificado as nrm, biseccion as bi


def f(x, subir_eje):
    return analisis.v(x) - (analisis.v(2*4.25) * subir_eje)

def f1(x):
    return analisis.v(x) - (analisis.v(2*4.25) * 0.5438596491)

def f2(x):
    return analisis.v(x) - analisis.v(2 * 4.25)

x1 = [0]
y1 = [f1(0)]

x2 = [0]
y2 = [f2(0)]

dx = [0]
dy = [analisis.derivada(0)]

for i in range(1, 8):
    x1.append(i)
    y1.append(f1(i))

    x2.append(i)
    y2.append(f2(i))

    dx.append(i)
    dy.append(analisis.derivada(i))

x1.append(2 * 4.25)
y1.append(f1(2 * 4.25))

x2.append(2 * 4.25)
y2.append(f2(2 * 4.25))

dx.append(2 * 4.25)
dy.append(analisis.derivada(2 * 4.25))

'''plt.figure()
plt.plot(x1, y1)
plt.show()'''

'''plt.figure()
plt.plot(x2, y2)
plt.show()'''

'''plt.figure()
plt.plot(dx, dy)
plt.show()'''

biseccion1 = bi.raiz(f1, 0, 2*4.25, 1e-5, 12)
biseccion2 = bi.raiz(f2, 0, 2*4.25, 1e-5, 12)

'''pfijo1 = pf.raiz(f1, 0, 1e-5, 12)
pfijo2 = pf.raiz(f2, 0, 1e-5, 12)'''

nr1 = nr.raiz(f1, analisis.derivada, 1e-12, 2*4.25 - 1e-12, 1e-5, 12) #lo corro un poco ya que derivada en extremos se anula
nr2 = nr.raiz(f2, analisis.derivada, 1e-12, 2*4.25, 1e-5, 12)

secante1 = se.raiz(f1, 0, 2*4.25, 1e-5, 12)
secante2 = se.raiz(f2, 0, 2*4.25, 1e-5, 12)

nr_modificado1 = nrm.raiz(f1, analisis.derivada, analisis.derivada_segunda, 1e-12, 2*4.25 - 1e-12, 1e-5, 12)
nr_modificado2 = nrm.raiz(f2, analisis.derivada, analisis.derivada_segunda, 1e-12, 2*4.25 - 1e-12, 1e-5, 12)

print("----------------BISECCION------------------")

print(biseccion1)
print(biseccion2)

'''print("-----------------PFIJO-----------------")

print(pfijo1)
print(pfijo2)'''

print("-------------------NR---------------")

print(nr1)
print(nr2)

print("-------------------SECANTE---------------")

print(secante1)
print(secante2)

print("-------------------NR MODFICIADO---------------")

print(nr_modificado1)
print(nr_modificado2)


