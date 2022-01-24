from time import time
import numpy as np

np_array =np.arange(1000000)
lista = list(range(1000000))

ini = time()
for _ in range (100): np_array *=2
fim = time()

print(f'Tempo em segundos usando NUMPY: {fim-ini}')

ini = time()
for _ in range (100): lista=[x*2 for x in lista]
fim = time()
print(f'Tempo em segundos usando Lista: {fim-ini}')