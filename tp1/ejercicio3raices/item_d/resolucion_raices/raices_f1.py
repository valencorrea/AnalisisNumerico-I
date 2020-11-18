from tp1.ejercicio3raices.item_a.f1_volumen_tanque import f1
import tp1.ejercicio3raices.item_d.metodos.biseccion  as bi
import tp1.ejercicio3raices.item_d.metodos.newton_raphson as nr
import tp1.ejercicio3raices.item_d.metodos.newton_raphson_modificado as nrm
import tp1.ejercicio3raices.item_d.metodos.secante as se
import tp1.ejercicio3raices.item_d.metodos.punto_fijo as pf
import tp1.ejercicio3raices.analisis_problema_fisico as analisis

pfijo1 = pf.raiz(f1, 4, 1e-13, 60)
biseccion1 = bi.raiz(f1, 0, 2*4.25, 1e-13, 60)
nr1 = nr.raiz(f1, analisis.derivada, 0, 2*4.25, 1e-13, 60)
secante1 = se.raiz(f1, 0, 2*4.25, 1e-13, 60)
nr_modificado1 = nrm.raiz(f1, analisis.derivada, analisis.derivada_segunda, 0, 2*4.25, 1e-13, 60)

