import pandas as pd

dataset=pd.read_csv('D:\Meus Documentos\Documentos\GitHub\CursosAlura\PythonDataScience\part2\db.csv',sep=';',index_col=0)

#Seleção Simples 
"""print(dataset.Motor)"""

#----------------------Consultas
"""select=dataset.Motor=='Motor Diesel'        #retorna Series
print(dataset[select])
    
print(dataset[(dataset.Motor=='Motor Diesel')&(dataset.Zero_km==True)])     #COnsulta"""

#----------------------Consultas Usando QUERY
print(dataset.query('Motor == "Motor Diesel" and Zero_km == True'))
#dataset.query('Motor == "Motor Diesel" and Zero_km == True')