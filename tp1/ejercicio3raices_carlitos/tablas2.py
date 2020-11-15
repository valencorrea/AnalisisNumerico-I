import resolucion
import pandas as pd
import plotly.figure_factory as ff


biseccion2, secante2, nr2, nr_modificado2 = resolucion.valores_f2()
ordenb2, orden_secante2, orden_nr2, orden_nr_modificado2 = resolucion.ordenes_f2()

biseccion = {'Raices': biseccion2[0][0:26], 'Cotas': biseccion2[1][0:26], 'Orden de convergencia': ordenb2}
secante = {'Raices': secante2[0], 'Cotas': secante2[1], 'Orden de convergencia': orden_secante2}
nr = {'Raices': nr2[0][2:26], 'Cotas': nr2[1][2:26], 'Orden de convergencia': orden_nr2}
nr_mod = {'Raices': nr_modificado2[0][2:5], 'Cotas': nr_modificado2[1][2:5], 'Orden de convergencia': orden_nr_modificado2}

print(len(nr_modificado2[0][0:26]), len(orden_nr_modificado2))


df1 = pd.DataFrame(biseccion, columns = ['Raices', 'Cotas', 'Orden de convergencia'])
df1.to_csv("biseccion2.csv")

df1 = pd.read_csv("biseccion2.csv")

df2 = pd.DataFrame(secante, columns = ['Raices', 'Cotas', 'Orden de convergencia'])
df2.to_csv("secante2.csv")

df2 = pd.read_csv("secante2.csv")

df3 = pd.DataFrame(nr, columns = ['Raices', 'Cotas', 'Orden de convergencia'])
df3.to_csv("newton_raphson2.csv")

df3 = pd.read_csv("newton_raphson2.csv")

df4 = pd.DataFrame(nr_mod, columns = ['Raices', 'Cotas', 'Orden de convergencia'])
df4.to_csv("newton_raphson_modificado2.csv")

df4 = pd.read_csv("newton_raphson_modificado2.csv")

print(df4)
