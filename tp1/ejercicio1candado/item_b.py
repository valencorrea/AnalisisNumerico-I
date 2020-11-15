import ejercicio1candado.item_a as fb

def realizar_fuerza_bruta(numero):
    comb_descubierta = False
    comb_a_probar = 0
    while comb_descubierta == False:
        if (comb_a_probar == numero):
            comb_descubierta = True
            print("La clave encontrada es:",comb_a_probar)
        comb_a_probar += 1

def adivinar_clave():
    numero = fb.definir_clave()
    realizar_fuerza_bruta(numero)

adivinar_clave()