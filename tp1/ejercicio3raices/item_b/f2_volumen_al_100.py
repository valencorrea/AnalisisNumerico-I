import tp1.ejercicio3raices.analisis_problema_fisico as analisis

def f2(x):
    # Quiero ver el volumen en 2R cuando el tanque se encuentra lleno al 100%
    return analisis.v(x) - (analisis.v(2 * 4.25) * 1)
