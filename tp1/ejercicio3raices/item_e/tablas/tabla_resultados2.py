from tp1.ejercicio3raices.item_d.resolucion_raices.raices_f2 import biseccion2
from tp1.ejercicio3raices.item_d.resolucion_raices.raices_f2 import nr2
from tp1.ejercicio3raices.item_d.resolucion_raices.raices_f2 import secante2
from tp1.ejercicio3raices.item_d.resolucion_raices.raices_f2 import nr_modificado2
from tp1.ejercicio3raices.item_d.resolucion_raices.raices_f2 import pfijo2
from tp1.ejercicio3raices.item_e.ordenes.convergencia_f2 import orden_pf2
from tp1.ejercicio3raices.item_e.ordenes.convergencia_f2 import ordenb2
from tp1.ejercicio3raices.item_e.ordenes.convergencia_f2 import orden_nr2
from tp1.ejercicio3raices.item_e.ordenes.convergencia_f2 import orden_secante2
from tp1.ejercicio3raices.item_e.ordenes.convergencia_f2 import orden_nr_modificado2
import tp1.ejercicio3raices.item_e.constantes_asintoticas.constante_f2 as c2
import pandas as pd

biseccion = {'Raices': biseccion2[0], 'Cotas': biseccion2[1], 'Orden de convergencia': ordenb2,'constante asintotica' : c2.lambda_b2}
pfijo = {'Raices': pfijo2[0], 'Cotas': pfijo2[1], 'Orden de convergencia': orden_pf2,'constante asintotica' : c2.lambda_pf2}
secante = {'Raices': secante2[0], 'Cotas': secante2[1], 'Orden de convergencia': orden_secante2,'constante asintotica' : c2.lambda_secante2[0]*1}
nr = {'Raices': nr2[0], 'Cotas': nr2[1], 'Orden de convergencia': orden_nr2,'constante asintotica' : c2.lambda_nr2}
nr_mod = {'Raices': nr_modificado2[0], 'Cotas': nr_modificado2[1], 'Orden de convergencia': orden_nr_modificado2,'constante asintotica' : c2.lambda_nr_modificado2}


df1 = pd.DataFrame(biseccion, columns = ['Raices', 'Cotas', 'Orden de convergencia','constante asintotica'])
df1.to_csv("biseccion2.csv")

df1 = pd.read_csv("biseccion2.csv")

df2 = pd.DataFrame(secante, columns = ['Raices', 'Cotas', 'Orden de convergencia','constante asintotica'])
df2.to_csv("secante2.csv")

df2 = pd.read_csv("secante2.csv")

df3 = pd.DataFrame(nr, columns = ['Raices', 'Cotas', 'Orden de convergencia','constante asintotica'])
df3.to_csv("newton_raphson2.csv")

df3 = pd.read_csv("newton_raphson2.csv")

df4 = pd.DataFrame(nr_mod, columns = ['Raices', 'Cotas', 'Orden de convergencia','constante asintotica'])
df4.to_csv("newton_raphson_modificado2.csv")


df5 = pd.DataFrame(pfijo, columns = ['Raices', 'Cotas', 'Orden de convergencia','constante asintotica'])
df5.to_csv("puntofijo2.csv")
