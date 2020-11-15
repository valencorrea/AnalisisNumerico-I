import resolucion
import pandas as pd
import plotly.figure_factory as ff


biseccion1, secante1, nr1, nr_modificado1 = resolucion.valores_f1()
lambda_b1, lambda_secante1, lambda_nr1, lambda_nr_modificado1 = resolucion.lambdas_f1()
ordenb1, orden_secante1, orden_nr1, orden_nr_modificado1 = resolucion.ordenes_f1()

biseccion = {'Raices': biseccion1[0][0:49], 'Cotas': biseccion1[1][0:49], 'Orden de convergencia': ordenb1}
secante = {'Raices': secante1[0][2:8], 'Cotas': secante1[1][2:8], 'Orden de convergencia': orden_secante1}
nr = {'Raices': nr1[0][2:6], 'Cotas': nr1[1][2:6], 'Orden de convergencia': orden_nr1}
nr_mod = {'Raices': nr_modificado1[0][2:6], 'Cotas': nr_modificado1[1][2:6], 'Orden de convergencia': orden_nr_modificado1}

print(len(nr_modificado1[0]), len(orden_nr_modificado1))


df1 = pd.DataFrame(biseccion, columns = ['Raices', 'Cotas', 'Orden de convergencia'])
df1.to_csv("biseccion1.csv")

df1 = pd.read_csv("biseccion1.csv")

df2 = pd.DataFrame(secante, columns = ['Raices', 'Cotas', 'Orden de convergencia'])
df2.to_csv("secante1.csv")

df2 = pd.read_csv("secante1.csv")

df3 = pd.DataFrame(secante, columns = ['Raices', 'Cotas', 'Orden de convergencia'])
df3.to_csv("newton_raphson1.csv")

df3 = pd.read_csv("newton_raphson1.csv")

df4 = pd.DataFrame(secante, columns = ['Raices', 'Cotas', 'Orden de convergencia'])
df4.to_csv("newton_raphson_modificado1.csv")

df4 = pd.read_csv("newton_raphson_modificado1.csv")

print(df4)






