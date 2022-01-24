import pandas as pd

dataset=pd.read_csv('D:\Meus Documentos\Documentos\GitHub\CursosAlura\PythonDataScience\part2\db.csv',sep=';',index_col=0)

"""print(dataset.head())      Imprime os primeiros 5 da tabela
print(dataset['Valor'].head())      #Retorna uma Series
print(dataset[['Valor']].head())      #Retorna um DataFrame
"""

#-----------------------------------Fazendo Iteração
"""
print(dataset[0:3]) #não pega o ultimo elemento, Que seria o '3'"""



#-----------------------------------Função LOC  -> Chama pelo INDEX(o rotulo)
"""
print(dataset.loc['Passat'])    #Retorna a linha que deseja

print(dataset.loc[['Passat','DS5']])    #Para retornar 2 linhas

print(dataset.loc[['Passat','DS5'],['Motor','Valor']]) #para retornar apenas a variavel que deseja"""


#-----------------------------------Função ILOC  -> Chama pelo INDICE
"""print(dataset.iloc[1])          #Formato de Series
print(dataset.iloc[[1]])        #Formato de DataFrame"""
#iterando ILOC
print(dataset.iloc[0:4])          
