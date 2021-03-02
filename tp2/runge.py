import numpy as np
import matplotlib.pyplot as plt

def rungekutta4_fg(fx,gx,x0,y0,z0,h,muestras):
    tamano = muestras + 1
    estimado = np.zeros(shape=(tamano,3),dtype=float)

    # incluye el punto [x0,y0]
    estimado[0] = [x0,y0,z0]
    xi = x0
    yi = y0
    zi = z0

    for i in range(1,tamano,1):
        K1y = h * fx(xi,yi,zi)
        K1z = h * gx(xi,yi,zi)

        K2y = h * fx(xi+h/2, yi + K1y/2, zi + K1z/2)
        K2z = h * gx(xi+h/2, yi + K1y/2, zi + K1z/2)

        K3y = h * fx(xi+h/2, yi + K2y/2, zi + K2z/2)
        K3z = h * gx(xi+h/2, yi + K2y/2, zi + K2z/2)

        K4y = h * fx(xi+h, yi + K3y, zi + K3z)
        K4z = h * gx(xi+h, yi + K3y, zi + K3z)

        yi = yi + (K1y+2 * K2y+2 * K3y+K4y)/6
        zi = zi + (K1z+2 * K2z+2 * K3z+K4z)/6
        xi = xi + h

        estimado[i] = [xi,yi,zi]
    return(estimado)

# INGRESO
# Parámetros de las ecuaciones
a = 1.2
b = 0.6
c = 0.8
d = 0.3

# Ecuaciones
f = lambda t,x,y : a * x - b * x * y
g = lambda t,x,y : - d * y + c * x * y

# Condiciones iniciales
t0 = 0
x0 = 2
y0 = 1

# parámetros del algoritmo
h = 0.1
muestras = 300

# PROCEDIMIENTO
tabla = rungekutta4_fg(f,g,t0,x0,y0,h,muestras)
ti = tabla[:,0]
xi = tabla[:,1]
yi = tabla[:,2]

# SALIDA
np.set_printoptions(precision=6)
print(' [ ti, xi, yi]')
print(tabla)


plt.plot(ti,xi, label='xi presa')
plt.plot(ti,yi, label='yi predador')

plt.xlim(0, 30)
plt.ylim(0, 7)

plt.title('predador-presa')
plt.xlabel('t tiempo')
plt.legend()
plt.grid()
plt.show()

# gráfica xi vs yi
plt.plot(xi,yi)

plt.title('presa-predador')
plt.xlabel('presa')
plt.ylabel('depredador')
plt.grid()
plt.show()