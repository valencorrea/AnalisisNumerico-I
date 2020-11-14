import matplotlib.pyplot as plt
import analisis_problema_fisico as analisis
import orden_convergencia as orden
import calculo_lambda as calc

import biseccion as bi
import punto_fijo as pf
import newton_raphson as nr
import secante as se
import newton_raphson_modificado as nrm

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

x1.append(2*4.25)
y1.append(f1(2*4.25))

x2.append(2*4.25)
y2.append(f2(2*4.25))

dx.append(2*4.25)
dy.append(analisis.derivada(2*4.25))

'''plt.figure()
plt.plot(x1, y1)
plt.show()

plt.figure()
plt.plot(x2, y2)
plt.show()

plt.figure()
plt.plot(dx, dy)
plt.show()'''

biseccion1 = bi.raiz(f1, 0, 2*4.25, 1e-13, 50)
biseccion2 = bi.raiz(f2, 0, 2*4.25, 1e-13, 50)
ordenb1 = orden.estimar_ordenar_convergencia(biseccion1[0], len(biseccion1[0]))
ordenb2 = orden.estimar_ordenar_convergencia(biseccion2[0], len(biseccion2[0]))
lambda_b1 = calc.calcular_lambda(ordenb1[len(ordenb1)-1], biseccion1[0][len(biseccion1[0]) - 1], biseccion1[0][len(biseccion1[0]) - 2])
lambda_b2 = calc.calcular_lambda(ordenb2[len(ordenb2)-1], biseccion2[0][len(biseccion2[0]) - 1], biseccion2[0][len(biseccion2[0]) - 2])


#pfijo1 = pf.raiz(f1, 0, 1e-13, 50)
#pfijo2 = pf.raiz(f2, 0, 1e-13, 50)
#ordenpf1 = orden.estimar_ordenar_convergencia(pfijo1[0], len(pfijo1[0]))
#ordenpf2 = orden.estimar_ordenar_convergencia(pfijo2[0], len(pfijo2[0]))


nr1 = nr.raiz(f1, analisis.derivada, 1e-12, 2*4.25 - 1e-12, 1e-13, 50)
nr2 = nr.raiz(f2, analisis.derivada, 1e-12, 2*4.25 - 1e-12, 1e-13, 50)
orden_nr1 = orden.estimar_ordenar_convergencia(nr1[0], len(nr1[0]))
orden_nr2 = orden.estimar_ordenar_convergencia(nr2[0], len(nr2[0]))
lambda_nr1 = calc.calcular_lambda(orden_nr1[len(orden_nr1)-1], nr1[0][len(nr1[0]) - 1], nr1[0][len(nr1[0]) - 2])
lambda_nr2 = calc.calcular_lambda(orden_nr2[len(orden_nr2)-1], nr2[0][len(nr2[0]) - 1], nr2[0][len(nr2[0]) - 2])

secante1 = se.raiz(f1, 0, 2*4.25, 1e-13, 50)
secante2 = se.raiz(f2, 0, 2*4.25, 1e-13, 50)
orden_secante1 = orden.estimar_ordenar_convergencia(secante1[0], len(secante1[0]))
orden_secante2 = orden.estimar_ordenar_convergencia(secante2[0], len(secante2[0]))
lambda_secante1 = calc.calcular_lambda(orden_secante1[len(orden_secante1)-1], secante1[0][len(secante1[0]) - 1], secante1[0][len(secante1[0]) - 2])
lambda_secante2 = calc.calcular_lambda(orden_secante2[len(orden_secante2)-1], secante2[0][len(secante2[0]) - 1], secante2[0][len(secante2[0]) - 2])


nr_modificado1 = nrm.raiz(f1, analisis.derivada, analisis.derivada_segunda, 1e-12, 2*4.25 - 1e-12, 1e-13, 50)
nr_modificado2 = nrm.raiz(f2, analisis.derivada, analisis.derivada_segunda, 1e-12, 2*4.25 - 1e-12, 1e-13, 50)
orden_nr_modificado1 = orden.estimar_ordenar_convergencia(nr_modificado1[0], len(nr_modificado1[0]))
orden_nr_modificado2 = orden.estimar_ordenar_convergencia(nr_modificado2[0], len(nr_modificado2[0]))
lambda_nr_modificado1 = calc.calcular_lambda(orden_nr_modificado1[len(orden_nr_modificado1)-1], nr_modificado1[0][len(nr_modificado1[0]) - 1], nr_modificado1[0][len(nr_modificado1[0]) - 2])
lambda_nr_modificado2 = calc.calcular_lambda(orden_nr_modificado2[len(orden_nr_modificado2)-1], nr_modificado2[0][len(nr_modificado2[0]) - 1], nr_modificado2[0][len(nr_modificado2[0]) - 2])

print("----------------BISECCION------------------")

print(biseccion1)
print(biseccion2)
print(ordenb1)
print(ordenb2)
print(lambda_b1)
print(lambda_b2)

'''print("-----------------PFIJO-----------------")

print(pfijo1)
print(pfijo2)'''

print("-------------------NR---------------")

print(nr1)
print(nr2)
print(orden_nr1)
print(orden_nr2)
print(lambda_nr1)
print(lambda_nr2)

print("-------------------SECANTE---------------")

print(secante1)
print(secante2)
print(orden_secante1)
print(orden_secante2)
print(lambda_secante1)
print(lambda_secante2)

print("-------------------NR MODFICIADO---------------")

print(nr_modificado1)
print(nr_modificado2)
print(orden_nr_modificado1)
print(orden_nr_modificado2)
print(lambda_nr_modificado1)
print(lambda_nr_modificado2)



'''-------------------------------------------ITEM G---------------------------------------------'''

plt.figure()


plt.plot(ordenb1[:], '-', lw=2, label='Biseccion')
plt.plot(orden_nr1[:], '-', lw=2, label='NR')
plt.plot(orden_nr_modificado1[:], '-', lw=2, label='Newton-Raphson modificado')
plt.plot(orden_secante1[:], '-', lw=2, label='Secante')

plt.xlabel('Paso [n]')
plt.ylabel('alfa')

plt.legend(loc='best')
plt.grid(True)

plt.show()

plt.figure()


plt.plot(ordenb2[:], '-', lw=2, label='Biseccion')
plt.plot(orden_nr2[:], '-', lw=2, label='NR')
plt.plot(orden_nr_modificado2[:], '-', lw=2, label='Newton-Raphson modificado')
plt.plot(orden_secante2[:], '-', lw=2, label='Secante')

plt.xlabel('Paso [n]')
plt.ylabel('alfa')

plt.legend(loc='best')
plt.grid(True)

plt.show()



def ordenes_f1():
    return ordenb1, orden_secante1, orden_nr1, orden_nr_modificado1

def ordenes_f2():
    return ordenb2, orden_secante2, orden_nr2, orden_nr_modificado2

def valores_f1():
    return biseccion1, secante1, nr1, nr_modificado1

def valores_f2():
    return biseccion2, secante2, nr2, nr_modificado2

def lambdas_f1():
    return lambda_b1, lambda_secante1, lambda_nr1, lambda_nr_modificado1

def lambdas_f2():
    return lambda_b2, lambda_secante2, lambda_nr2, lambda_nr_modificado2

