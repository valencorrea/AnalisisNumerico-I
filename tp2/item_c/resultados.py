from item_c.maximos import maximos_depredador
from item_c.maximos import maximos_presa

resultados_x = maximos_presa()
resultados_y = maximos_depredador()

picos_presa = resultados_x[]
picos_depredador = resultados_y[]

tiempo = resultados[:,0]
presa = resultados[:,1]
depredador = resultados[:,2]

tabla = {'presa': picos_presa}
df1 = pd.DataFrame(tabla, columns = ['presa')
df1.to_csv("resultados_item_c.csv", float_format='{0:.7f}'.format)