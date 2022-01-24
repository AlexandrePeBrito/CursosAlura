import pandas as pd

#   pd.set_option('display.max_rows',300)
#pd.set_option('display.max_columns',300)
dataset=pd.read_csv('D:\Meus Documentos\Documentos\GitHub\Alura\PythonDataScience\part2\db.csv',sep=';')

print(dataset[['Quilometragem','Valor']].describe())