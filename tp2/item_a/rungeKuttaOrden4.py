import numpy as np

def runge_kutta(f_1, f_2, x, y, h, t_0, cota_t):
    soluciones_x = [x]
    soluciones_y = [y]
    t = [t_0]
    iteracion = 1
    t_i = t_0

    # m -> x
    # k -> y

    for t_i in range(1,cota_t + 1, 1):
        m_1 = h * f_1(t_i, x, y)
        k_1 = h * f_2(t_i, x, y)

        m_2 = h * f_1(t_i + (h * 0.5), x + (0.5 * m_1), y + (0.5 * k_1))
        k_2 = h * f_2(t_i + (h * 0.5), x + (0.5 * m_1), y + (0.5 * k_1))

        m_3 = h * f_1(t_i + (h * 0.5), x + (0.5 * m_2), y + (0.5 * k_2))
        k_3 = h * f_2(t_i + (h * 0.5), x + (0.5 * m_2), y + (0.5 * k_2))

        m_4 = h * f_1(t_i + h, x + m_3, y + k_3)
        k_4 = h * f_2(t_i + h, x + m_3, y + k_3)

        x = np.round(x + ((m_1 + (2 * m_2) + (2 * m_3) + m_4) / 6), 7)
        soluciones_x.append(x)

        y = np.round(y + ((k_1 + (2 * k_2) + (2 * k_3) + k_4) / 6), 7)
        soluciones_y.append(y)

        t_i = np.round((iteracion * h), 1)
        t.append(t_i)

        iteracion = iteracion + 1

    return t, soluciones_x, soluciones_y
'''

def runge_kutta(fx,gx,x0,y0,z0,h,muestras):
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
'''