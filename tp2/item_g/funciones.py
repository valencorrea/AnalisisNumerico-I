def derivada_x(t, x, y, a, b):

    # a = 1.2
    # b = 0.6
    return (a * x) - (b * x * y)


def derivada_y(t, x, y, c, d):

    # c = 0.3
    # d = 0.8
    # hay un error de enunciado, habia que intercambiarlos
    return (c * x * y) - (d * y)