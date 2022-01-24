import numpy as np

km= np.loadtxt('D:\Meus Documentos\Documentos\GitHub\Alura\PythonDataScience\PythonNumpy\carros-km.txt')
anos=np.loadtxt('D:\Meus Documentos\Documentos\GitHub\Alura\PythonDataScience\PythonNumpy\carros-anos.txt', dtype= int)

km_media=km/(2019-anos)
print(km_media)