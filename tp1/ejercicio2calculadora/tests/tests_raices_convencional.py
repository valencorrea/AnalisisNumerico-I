from tp1.ejercicio2calculadora.modelo import raices_convencional as rc
a = [1, 1, 1000, 1, 1000, 1000, 1000, 0.000000000000001, 1]
b = [10000000000000, 2, 10000000, 1000000000000000, 100000000000, 10000000000, 10000000, 10000000010, 1e32]
c = [1, 1, 1, 0.00001, 1, 1, 1, 10, 1]
pruebasx_1 = []
pruebasx_2 = []

for i in range(len(a)):
        prueba = rc.raices(a[i],b[i],c[i])
        pruebasx_1.append( prueba[0])
        pruebasx_2.append( prueba[1])
