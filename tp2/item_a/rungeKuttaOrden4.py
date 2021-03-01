def runge_kutta(f, variable, h, t_0, cota_t):
    resultados = [variable]
    iteracion = 1
    t_i = t_0
    t = [t_i]

    while(t_i < cota_t):
        k_1 = h * f(t_i, variable)
        k_2 = h * f(t_i + (h/2), variable + (1/2) * k_1)
        k_3 = h * f(t_i + (h/2), variable + (1/2) * k_2)
        k_4 = h * f(t_i + h, variable + k_3)

        variable = variable + ((k_1 + 2 * k_2 + 2 * k_3 + k_4) / 6)
        resultados.append(variable)

        t_i = t_0 + (iteracion * h)
        t.append(t_i)

        iteracion = iteracion + 1

    return (t, resultados)