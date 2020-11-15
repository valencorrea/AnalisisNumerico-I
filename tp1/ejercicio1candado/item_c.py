import matplotlib.pyplot as plt
import random

def realizar_experimento():
    cant_experimentos = 100000
    cant_intentos = [0] * (cant_experimentos)
    cant_combinaciones = 10000

    for num_experim in range(0, cant_experimentos - 1):
        numero = int(random.random() * (cant_combinaciones - 1))
        comb_descubierta = False
        comb_a_probar = 0
        while comb_descubierta == False:
            if (comb_a_probar == numero):
                comb_descubierta = True
                cant_intentos[num_experim] = comb_a_probar + 1
            comb_a_probar += 1

    long_bins = 10
    plt.figure(figsize=(15, 8))
    plt.hist(cant_intentos, bins=int(cant_combinaciones / long_bins), range=(0, cant_combinaciones - 1))
    plt.title('Histograma de cantidad de intentos realizados para hallar la combinación')
    plt.xlabel('Cantidad de intentos agrupados de 10 en 10')
    plt.show()


realizar_experimento()