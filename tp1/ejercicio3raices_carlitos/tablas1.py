import resolucion
import pandas as pd
import plotly.figure_factory as ff


biseccion1, secante1, nr1, nr_modificado1 = resolucion.valores_f1()
lambda_b1, lambda_secante1, lambda_nr1, lambda_nr_modificado1 = resolucion.lambdas_f1()
ordenb1, orden_secante1, orden_nr1, orden_nr_modificado1 = resolucion.ordenes_f1()

biseccion = {'Raices': biseccion1[0], 'Cotas': biseccion1[1], 'Orden de convergencia': ordenb1}
secante = {'Raices': secante1[0], 'Cotas': secante1[1], 'Orden de convergencia': orden_secante1}
nr = {'Raices': nr1[0], 'Cotas': nr1[1], 'Orden de convergencia': orden_nr1}
nr_mod = {'Raices': nr_modificado1[0], 'Cotas': nr_modificado1[1], 'Orden de convergencia': orden_nr_modificado1}



df1 = pd.DataFrame()
df1['Raices'] = biseccion1[0][0:49]
df1['Cotas'] = biseccion1[1][0:49]
df1['Orden de convergencia'] = ordenb1


fig =  ff.create_table(df1)
fig.update_layout(
    autosize=False,
    width=500,
    height=200,
)
fig.write_image("biseccion1.png", scale=2)







