import tp1.ejercicio3raices.item_e.constantes_asintoticas.calculo_lambda as calc
import tp1.ejercicio3raices.item_d.resolucion_raices.raices_f1 as modos
import tp1.ejercicio3raices.item_e.ordenes.convergencia_f1 as orden

lambda_b1 = calc.calcular_lambda(orden.ordenb1, modos.biseccion1[0])
lambda_nr1 = calc.calcular_lambda(orden.orden_nr1, modos.nr1[0])
lambda_secante1 = calc.calcular_lambda(orden.orden_secante1, modos.secante1[0])
lambda_nr_modificado1 = calc.calcular_lambda(orden.orden_nr_modificado1, modos.nr_modificado1[0])
