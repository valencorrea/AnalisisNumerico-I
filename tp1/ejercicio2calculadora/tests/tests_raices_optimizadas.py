from modelo import raices_optimizadas as ro
a = [1, 1, 1000, 1, 1000, 1000, 1000, 0.000000000000001, 1]
b = [10000000000000, 2, 10000000, 1000000000000000, 100000000000, 10000000000, 10000000, 10000000010, 1e32]
c = [1, 1, 1, 0.00001, 1, 1, 1, 10, 1]
pruebasx_1 = []
pruebasx_2 = []

for i in range(len(a)):
        prueba = ro.raices_optimizadas(a[i],b[i],c[i])
        pruebasx_1.append( prueba[0])
        pruebasx_2.append( prueba[1])
# p1 = ro.raices_optimizadas(1, 10000000000000, 1)
#
# p2 = ro.raices_optimizadas(1, 2, 1)
#
# p3 = ro.raices_optimizadas(1000, 10000000, 1)
#
# p4 = ro.raices_optimizadas(1, 1000000000000000, 0.00001)
#
# p5 = ro.raices_optimizadas(1000, 100000000000, 1)
#
# p6 = ro.raices_optimizadas(1000, 10000000000, 1)
#
# p7 = ro.raices_optimizadas(1000, 10000000, 1)
#
# p8 = ro.raices_optimizadas(0.000000000000001, 10000000010, 10)
#
# p9 = ro.raices_optimizadas(1, 1e32, 1)

# try:
#
#     ro.raices_optimizadas(0, 10000000010, 10)
#
# except:
#
#     print(sys.exc_info()[1])  # no se ingreso un polinomio de grado 2
#
# try:
#
#     ro.raices_optimizadas(1, 0, 10)
#
# except:
#
#     print(sys.exc_info()[1])  # no se pueden calcular raices negativas

# data = {'a': [1, 1, 1000, 1, 1000, 1000, 1000, 0.000000000000001, 1],
#         'b': [10000000000000, 2, 10000000, 1000000000000000, 100000000000, 10000000000, 10000000, 10000000010, 1e32],
#         'c': [1, 1, 1, 0.00001, 1, 1, 1, 10, 1],
#         'x1': [p1[0], p2[0], p3[0], p4[0], p5[0], p6[0], p7[0], p8[0], p9[0]],
#         'x2': [p1[1], p2[1], p3[1], p4[1], p5[1], p6[1], p7[1], p8[1], p9[1]]}

