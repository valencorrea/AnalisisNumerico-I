import ejercicio3raices.item_e.constantes_asintoticas.calculo_lambda as calc
from ejercicio3raices.item_d.resolucion_raices.raices_f2 import biseccion2
from ejercicio3raices.item_d.resolucion_raices.raices_f2 import nr2
from ejercicio3raices.item_d.resolucion_raices.raices_f2 import secante2
from ejercicio3raices.item_d.resolucion_raices.raices_f2 import nr_modificado2
from ejercicio3raices.item_e.ordenes.convergencia_f2 import ordenb2
from ejercicio3raices.item_e.ordenes.convergencia_f2 import orden_nr2
from ejercicio3raices.item_e.ordenes.convergencia_f2 import orden_secante2
from ejercicio3raices.item_e.ordenes.convergencia_f2 import orden_nr_modificado2

lambda_b2 = calc.calcular_lambda(ordenb2[len(ordenb2)-1], biseccion2[0][len(biseccion2[0]) - 1], biseccion2[0][len(biseccion2[0]) - 2])
lambda_nr2 = calc.calcular_lambda(orden_nr2[len(orden_nr2)-1], nr2[0][len(nr2[0]) - 1], nr2[0][len(nr2[0]) - 2])
lambda_secante2 = calc.calcular_lambda(orden_secante2[len(orden_secante2)-1], secante2[0][len(secante2[0]) - 1], secante2[0][len(secante2[0]) - 2])
lambda_nr_modificado2 = calc.calcular_lambda(orden_nr_modificado2[len(orden_nr_modificado2)-1], nr_modificado2[0][len(nr_modificado2[0]) - 1], nr_modificado2[0][len(nr_modificado2[0]) - 2])
