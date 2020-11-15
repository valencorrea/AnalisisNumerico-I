import random

def definir_clave():
    cant_combinaciones = 10000
    numero = int(random.random()*(cant_combinaciones-1))
    print("La clave es:",numero)
    return numero
