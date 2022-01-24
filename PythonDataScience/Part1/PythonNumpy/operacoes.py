import numpy as np

km=[44410,5712,37123]
ano=[2003,1991,1990]

#ERROR -> Não aceita operações entre int e lista
#idade=2019-ano         
#print(idade)

km1=np.array([44410,5712,37123])
ano1=np.array([2003,1991,1990])

#Numpy aceita operações entre int e array
idade=2019-ano1
print(idade)

km_media=km1/idade
print(km_media)

