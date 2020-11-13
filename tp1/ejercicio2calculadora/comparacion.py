import tests_raices_convencional as convencional
import tests_raices_optimizadas as optimizadas
import pandas as pd

data = {'convencional': convencional.data(), 'optimizada': optimizadas.data()}

df = pd.DataFrame(data, columns = ['convencional', 'optimizada'])

df.to_csv('example.csv')

df = pd.read_csv('example.csv')
print()
print()
print(df)