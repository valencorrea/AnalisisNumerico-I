import matplotlib.pyplot as plt
import numpy as np


def v(x):
    return ((np.pi) * x**2) * (12.75 - x) / 3

# por que -3?
x = [-3]
y = [v(-3)]

def derivada(x):
    return (-np.pi * (x**2)) + (2 * 12.75 * np.pi * x / 3)

def derivada_segunda(x):
    return (-2 * np.pi * x) + (2 * 12.75 * np.pi / 3)

# si descomento esto se imprime dos veces cuando llamo a las de imprimir

'''
for i in range(-2,15):
    x.append(i)
    y.append(v(i))

plt.figure()
plt.plot(x, y)
plt.show()

print("hmax es: ", v(2*4.25))
'''
