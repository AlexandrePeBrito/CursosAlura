import pandas as pd

dados=pd.read_csv('D:/Meus Documentos/Documentos/GitHub/CursosAlura/PythonDataScience/tratandoDados/importando/aluguel.csv',sep=';')
tiposImoveis=dados['Tipo']
tiposImoveis.drop_duplicates(inplace=True)

tiposImoveis.index= range(0,tiposImoveis.shape[0]) #pegar de 0 ate o numero de elementos

print(tiposImoveis)
