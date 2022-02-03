import pandas as pd

dados=pd.read_csv('D:/Meus Documentos/Documentos/GitHub/CursosAlura/PythonDataScience/tratandoDados/importando/aluguel.csv',sep=';')
tiposImoveis=dados['Tipo']

print(type(tiposImoveis))   #Series

""" Series é uma coluna
    DataFrame é um conjunto de Series"""

print(tiposImoveis.drop_duplicates())       #mostra os tipos unicos