import numpy as np

km1=np.array([44410,5712,37123])
anos1=np.array([2003,1991,1990])

dados=np.array([km1,anos1])
print(dados)

km_media=dados[0]/(2019-dados[1])
print(km_media)