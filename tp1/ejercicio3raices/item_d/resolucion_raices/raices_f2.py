from tp1.ejercicio3raices.item_b.f2_volumen_al_100 import f2
import tp1.ejercicio3raices.item_d.metodos.biseccion  as bi
import tp1.ejercicio3raices.item_d.metodos.newton_raphson as nr
import tp1.ejercicio3raices.item_d.metodos.newton_raphson_modificado as nrm
import tp1.ejercicio3raices.item_d.metodos.secante as se
import tp1.ejercicio3raices.item_d.metodos.punto_fijo as pf
import tp1.ejercicio3raices.analisis_problema_fisico as analisis

pfijo2 = pf.raiz(f2, 4, 1e-13, 4)
biseccion2 = bi.raiz(f2, 0, 2*4.25, 1e-13, 50)
nr2 = nr.raiz(f2, analisis.derivada, 1e-12, 2*4.25 - 1e-12, 1e-13, 50)
secante2 = se.raiz(f2, 0, 2*4.25, 1e-13, 50)
nr_modificado2 = nrm.raiz(f2, analisis.derivada, analisis.derivada_segunda, 1e-12, 2*4.25 - 1e-12, 1e-13, 50)
# print(  F"{pfijo2} pf")
# print(F"{nr2}nr1")
