from ejercicio3raices.item_d.resolucion_raices.raices_f1 import biseccion1
from ejercicio3raices.item_d.resolucion_raices.raices_f1 import nr1
from ejercicio3raices.item_d.resolucion_raices.raices_f1 import secante1
from ejercicio3raices.item_d.resolucion_raices.raices_f1 import nr_modificado1
from ejercicio3raices.item_e.ordenes.convergencia_f1 import ordenb1
from ejercicio3raices.item_e.ordenes.convergencia_f1 import orden_nr1
from ejercicio3raices.item_e.ordenes.convergencia_f1 import orden_secante1
from ejercicio3raices.item_e.ordenes.convergencia_f1 import orden_nr_modificado1
import ejercicio3raices.item_e.constantes_asintoticas.constante_f1 as c1
import pandas as pd

biseccion = {'Raices': biseccion1[0][0:49], 'Cotas': biseccion1[1][0:49], 'Orden de convergencia': ordenb1,'constante asintotica' : [c1.lambda_b1]* 49 }
secante = {'Raices': secante1[0][2:8], 'Cotas': secante1[1][2:8], 'Orden de convergencia': orden_secante1,'constante asintotica' : [c1.lambda_secante1]*6}
nr = {'Raices': nr1[0][2:6], 'Cotas': nr1[1][2:6], 'Orden de convergencia': orden_nr1,'constante asintotica' : [c1.lambda_nr1]* 4}
nr_mod = {'Raices': nr_modificado1[0][2:6], 'Cotas': nr_modificado1[1][2:6], 'Orden de convergencia': orden_nr_modificado1,'constante asintotica' : [c1.lambda_nr_modificado1]* 4}

print(len(nr_modificado1[0]), len(orden_nr_modificado1))


df1 = pd.DataFrame(biseccion, columns = ['Raices', 'Cotas', 'Orden de convergencia','constante asintotica'])
df1.to_csv("biseccion1.csv")

df1 = pd.read_csv("biseccion1.csv")

df2 = pd.DataFrame(secante, columns = ['Raices', 'Cotas', 'Orden de convergencia','constante asintotica'])
df2.to_csv("secante1.csv")

df2 = pd.read_csv("secante1.csv")

df3 = pd.DataFrame(secante, columns = ['Raices', 'Cotas', 'Orden de convergencia','constante asintotica'])
df3.to_csv("newton_raphson1.csv")

df3 = pd.read_csv("newton_raphson1.csv")

df4 = pd.DataFrame(secante, columns = ['Raices', 'Cotas', 'Orden de convergencia','constante asintotica'])
df4.to_csv("newton_raphson_modificado1.csv")

df4 = pd.read_csv("newton_raphson_modificado1.csv")

print(df4)
