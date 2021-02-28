def runge_kutta(f, x_0, y_0, h, t_0, cota_t):
    resultados = []
    iteracion = 0
    t_i = 0
    t = []

    while(t_i < cota_t):
        k_1 = f(x_0, y_0)
        k_2 = f(x_0 + (h/2), y_0 + (1/2) * h * k_1)
        k_3 = f(x_0 + (h/2), y_0 + (1/2) * h * k_2)
        k_4 = f(x_0 + h, y_0 + h * k_3)

        y_0_mas_uno = y_0 + (h/6) * (k_1 + 2 * k_2 + 2 * k_3 + k_4)
        resultados.append(y_0_mas_uno)

        t_i = t_0 + (iteracion * h)
        t.append(t_i)

        iteracion+=1

    return (t, resultados)