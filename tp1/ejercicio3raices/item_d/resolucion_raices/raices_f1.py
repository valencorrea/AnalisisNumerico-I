from ejercicio3raices.item_a.f1_volumen_tanque import f1
import ejercicio3raices.item_d.biseccion  as bi
import ejercicio3raices.item_d.newton_raphson as nr
import ejercicio3raices.item_d.newton_raphson_modificado as nrm
import ejercicio3raices.item_d.secante as se
import ejercicio3raices.analisis_problema_fisico as analisis

#pfijo1 = pf.raiz(f1, 0, 1e-13, 50)
biseccion1 = bi.raiz(f1, 0, 2*4.25, 1e-13, 50)
nr1 = nr.raiz(f1, analisis.derivada, 1e-12, 2*4.25 - 1e-12, 1e-13, 50)
secante1 = se.raiz(f1, 0, 2*4.25, 1e-13, 50)
nr_modificado1 = nrm.raiz(f1, analisis.derivada, analisis.derivada_segunda, 1e-12, 2*4.25 - 1e-12, 1e-13, 50)
