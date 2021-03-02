import numpy as np

def runge_kutta(f_1, f_2, x, y, h, t_0, cota_t):
    soluciones_x = [x]
    soluciones_y = [y]
    t = [t_0]
    iteracion = 1
    t_i = t_0

    # m -> x
    # k -> y

    while t_i < cota_t:
        m_1 = h * f_1(t_i, x, y)
        k_1 = h * f_2(t_i, x, y)

        m_2 = h * f_1(t_i + (h/2), x + (1/2) * m_1, y + (1/2) * k_1)
        k_2 = h * f_2(t_i + (h/2), x + (1/2) * m_1, y + (1/2) * k_1)

        m_3 = h * f_1(t_i + (h/2), x + (1/2) * m_2, y + (1/2) * k_2)
        k_3 = h * f_2(t_i + (h/2), x + (1/2) * m_2, y + (1/2) * k_2)

        m_4 = h * f_1(t_i + h, x + m_3, y + k_3)
        k_4 = h * f_2(t_i + h, x + m_3, y + k_3)

        x = np.round(x + ((m_1 + 2 * m_2 + 2 * m_3 + m_4) / 6), 7)
        soluciones_x.append(x)

        y = np.round(y + ((k_1 + 2 * k_2 + 2 * k_3 + k_4) / 6), 7)
        soluciones_y.append(y)

        t_i = np.round(t_i + (iteracion * h), 1)
        t.append(t_i)

        iteracion = iteracion + 1

    return t, soluciones_x, soluciones_y