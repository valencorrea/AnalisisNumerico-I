import resolucion
import pandas as pd

biseccion2, secante2, nr2, nr_modificado2 = resolucion.valores_f2()

biseccion = {'Raices': biseccion2[0], 'Cotas': biseccion2[1]}
secante = {'Raices': secante2[0], 'Cotas': secante2[1]}
nr = {'Raices': nr2[0], 'Cotas': nr2[1]}
nr_mod = {'Raices': nr_modificado2[0], 'Cotas': nr_modificado2[1]}


df1 = pd.DataFrame(biseccion, columns = ['Raices', 'Cotas'])
df1.to_csv("punto2_biseccion.csv")
df1 = pd.read_csv("punto2_biseccion.csv")

df2 = pd.DataFrame(secante, columns = ['Raices', 'Cotas'])
df2.to_csv("punto2_secante.csv")
df2 = pd.read_csv("punto2_secante.csv")

df3 = pd.DataFrame(nr, columns = ['Raices', 'Cotas'])
df3.to_csv("punto2_nr.csv")
df3 = pd.read_csv("punto2_nr.csv")

df4 = pd.DataFrame(nr_mod, columns = ['Raices', 'Cotas'])
df4.to_csv("punto2_nr_mod.csv")
df4 = pd.read_csv("punto2_nr_mod.csv")


print()
print()
print(df4)







