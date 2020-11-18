from tp1.ejercicio2calculadora.tests import tests_raices_convencional as convencional, tests_raices_optimizadas as optimizadas
import pandas as pd

data = {'a': convencional.a,
        'b': convencional.b,
        'c': convencional.c,
        'convencional_x1': convencional.pruebasx_1,
        'convencional_x2': convencional.pruebasx_2,
        'optimizada_x1': optimizadas.pruebasx_1,
        'optimizada_x2': optimizadas.pruebasx_2
        }

df = pd.DataFrame(data, columns = ['a','b','c','convencional_x1','convencional_x2', 'optimizada_x1','optimizada_x2'])

decimals = pd.Series([7,7,7,7,7,7,7], index=['a','b','c','convencional_x1','convencional_x2', 'optimizada_x1','optimizada_x2'])
df.round(decimals)
df.to_csv("Tabla_de_comparacion.csv")

