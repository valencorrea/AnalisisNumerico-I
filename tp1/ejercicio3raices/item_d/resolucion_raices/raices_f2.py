from ejercicio3raices.item_b.f2_volumen_al_100 import f2
import ejercicio3raices.item_d.biseccion  as bi
import ejercicio3raices.item_d.newton_raphson as nr
import ejercicio3raices.item_d.newton_raphson_modificado as nrm
import ejercicio3raices.item_d.secante as se
import ejercicio3raices.analisis_problema_fisico as analisis

#pfijo2 = pf.raiz(f2, 0, 1e-13, 50)
biseccion2 = bi.raiz(f2, 0, 2*4.25, 1e-13, 50)
nr2 = nr.raiz(f2, analisis.derivada, 1e-12, 2*4.25 - 1e-12, 1e-13, 50)
secante2 = se.raiz(f2, 0, 2*4.25, 1e-13, 50)
nr_modificado2 = nrm.raiz(f2, analisis.derivada, analisis.derivada_segunda, 1e-12, 2*4.25 - 1e-12, 1e-13, 50)

print(nr2)
