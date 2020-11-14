import analisis_problema_fisico as analisis

def f1(x):

    # Quiero ver el volumen a partir de 2R y el porcentaje pedido
    return analisis.v(x) - (analisis.v(2 * 4.25) * 0.5438596491)
