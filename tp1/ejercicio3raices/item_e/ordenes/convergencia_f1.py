import tp1.ejercicio3raices.item_e.ordenes.orden_convergencia as orden
from tp1.ejercicio3raices.item_d.resolucion_raices.raices_f1 import biseccion1
from tp1.ejercicio3raices.item_d.resolucion_raices.raices_f1 import nr1
from tp1.ejercicio3raices.item_d.resolucion_raices.raices_f1 import secante1
from tp1.ejercicio3raices.item_d.resolucion_raices.raices_f1 import nr_modificado1

ordenb1 = orden.estimar_ordenar_convergencia(biseccion1[0], len(biseccion1[0]))
#ordenpf1 = orden.estimar_ordenar_convergencia(pfijo1[0], len(pfijo1[0]))
orden_nr1 = orden.estimar_ordenar_convergencia(nr1[0], len(nr1[0]))
orden_secante1 = orden.estimar_ordenar_convergencia(secante1[0], len(secante1[0]))
orden_nr_modificado1 = orden.estimar_ordenar_convergencia(nr_modificado1[0], len(nr_modificado1[0]))
