from os import sep
import pandas as pd

dados=pd.read_csv('D:/Meus Documentos/Documentos/GitHub/CursosAlura/PythonDataScience/tratandoDados/importando/aluguel.csv',sep=';')

#print(dados.info())

tiposDados=pd.DataFrame(dados.dtypes,columns=['Tipos de Dados'])
tiposDados.columns.name = 'Variaveis'
print(tiposDados)
print(dados.shape)      #Saber numero de elementos e variaveis  
