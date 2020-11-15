import ejercicio3raices.item_e.constantes_asintoticas.calculo_lambda as calc
from ejercicio3raices.item_d.resolucion_raices.raices_f1 import biseccion1
from ejercicio3raices.item_d.resolucion_raices.raices_f1 import nr1
from ejercicio3raices.item_d.resolucion_raices.raices_f1 import secante1
from ejercicio3raices.item_d.resolucion_raices.raices_f1 import nr_modificado1
from ejercicio3raices.item_e.ordenes.convergencia_f1 import ordenb1
from ejercicio3raices.item_e.ordenes.convergencia_f1 import orden_nr1
from ejercicio3raices.item_e.ordenes.convergencia_f1 import orden_secante1
from ejercicio3raices.item_e.ordenes.convergencia_f1 import orden_nr_modificado1

lambda_b1 = calc.calcular_lambda(ordenb1[len(ordenb1)-1], biseccion1[0][len(biseccion1[0]) - 1], biseccion1[0][len(biseccion1[0]) - 2])
lambda_nr1 = calc.calcular_lambda(orden_nr1[len(orden_nr1)-1], nr1[0][len(nr1[0]) - 1], nr1[0][len(nr1[0]) - 2])
lambda_secante1 = calc.calcular_lambda(orden_secante1[len(orden_secante1)-1], secante1[0][len(secante1[0]) - 1], secante1[0][len(secante1[0]) - 2])
lambda_nr_modificado1 = calc.calcular_lambda(orden_nr_modificado1[len(orden_nr_modificado1)-1], nr_modificado1[0][len(nr_modificado1[0]) - 1], nr_modificado1[0][len(nr_modificado1[0]) - 2])
