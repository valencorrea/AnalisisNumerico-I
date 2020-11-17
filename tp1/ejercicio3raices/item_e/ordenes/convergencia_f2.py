import tp1.ejercicio3raices.item_e.ordenes.orden_convergencia as orden
from tp1.ejercicio3raices.item_d.resolucion_raices.raices_f2 import biseccion2
from tp1.ejercicio3raices.item_d.resolucion_raices.raices_f2 import nr2
from tp1.ejercicio3raices.item_d.resolucion_raices.raices_f2 import secante2
from tp1.ejercicio3raices.item_d.resolucion_raices.raices_f2 import nr_modificado2

ordenb2 = orden.estimar_ordenar_convergencia(biseccion2[0], len(biseccion2[0]))
#ordenpf2 = orden.estimar_ordenar_convergencia(pfijo2[0], len(pfijo2[0]))
orden_nr2 = orden.estimar_ordenar_convergencia(nr2[0], len(nr2[0]))
orden_secante2 = orden.estimar_ordenar_convergencia(secante2[0], len(secante2[0]))
orden_nr_modificado2 = orden.estimar_ordenar_convergencia(nr_modificado2[0], len(nr_modificado2[0]))
