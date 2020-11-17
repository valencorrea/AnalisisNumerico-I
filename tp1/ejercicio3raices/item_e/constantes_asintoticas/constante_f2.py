import tp1.ejercicio3raices.item_e.constantes_asintoticas.calculo_lambda as calc
import tp1.ejercicio3raices.item_e.constantes_asintoticas.calculo_lambda_lineal as calc_lineal
import tp1.ejercicio3raices.item_d.resolucion_raices.raices_f2 as modos
import tp1.ejercicio3raices.item_e.ordenes.convergencia_f2 as orden


lambda_b2 = calc_lineal.calcular_lambda(orden.ordenb2, modos.biseccion2[0])
lambda_nr2 = calc.calcular_lambda(orden.orden_nr2, modos.nr2[0])
lambda_secante2 = calc.calcular_lambda(orden.orden_secante2, modos.secante2[0])
lambda_nr_modificado2 = calc.calcular_lambda(orden.orden_nr_modificado2, modos.nr_modificado2[0])
