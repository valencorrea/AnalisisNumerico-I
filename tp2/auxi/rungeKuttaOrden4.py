import numpy as np

def runge_kutta(fx, gx, x0, y0, z0, h, muestras):
    tamano = muestras + 1
    estimado = np.zeros(shape=(tamano, 3), dtype=float)

    # incluye el punto [x0,y0]
    estimado[0] = [x0, y0, z0]
    xi = x0
    yi = y0
    zi = z0

    for i in range(1, tamano, 1):
        K1y = h * fx(xi, yi, zi)
        K1z = h * gx(xi, yi, zi)

        K2y = h * fx(xi + h / 2, yi + K1y / 2, zi + K1z / 2)
        K2z = h * gx(xi + h / 2, yi + K1y / 2, zi + K1z / 2)

        K3y = h * fx(xi + h / 2, yi + K2y / 2, zi + K2z / 2)
        K3z = h * gx(xi + h / 2, yi + K2y / 2, zi + K2z / 2)

        K4y = h * fx(xi + h, yi + K3y, zi + K3z)
        K4z = h * gx(xi + h, yi + K3y, zi + K3z)

        yi = yi + (K1y + 2 * K2y + 2 * K3y + K4y) / 6
        zi = zi + (K1z + 2 * K2z + 2 * K3z + K4z) / 6
        xi = xi + h

        estimado[i] = [xi, yi, zi]

    return (estimado)