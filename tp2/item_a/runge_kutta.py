import numpy as np

def runge_kutta_orden4(f_1, f_2, t, x, y, h, tope_iteracion):

    indice = 0
    resultado = np.zeros(shape = (tope_iteracion, 3), dtype = float)
    resultado[0] = [t, x, y]

    # x -> m_n
    # y -> k_n

    while indice < tope_iteracion:
        m_1 = h * f_1(t, x, y)
        k_1 = h * f_2(t, x, y)

        m_2 = h * f_1(t + h * 0.5, x + m_1 * 0.5, y + k_1 * 0.5)
        k_2 = h * f_2(t + h * 0.5, x + m_1 * 0.5, y + k_1 * 0.5)

        m_3 = h * f_1(t + h * 0.5, x + m_2 * 0.5, y + k_2 * 0.5)
        k_3 = h * f_2(t + h * 0.5, x + m_2 * 0.5, y + k_2 * 0.5)

        m_4 = h * f_1(t + h * 0.5, x + m_3, y + k_3)
        k_4 = h * f_2(t + h * 0.5, x + m_3, y + k_3)

        x = x + (m_1 + (2 * m_2) + (2 * m_3) + m_4) / 6
        y = y + (k_1 + (2 * k_2) + (2 * k_3) + k_4) / 6
        t = t + h

        resultado[indice] = [t, x, y]
        indice += 1

    return resultado
