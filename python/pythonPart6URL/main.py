url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"

# Sanitização da URL
url = url.strip()

# Validação da URL
if url == "":
    raise ValueError("A URL está vazia")
interrogacao=url.find('?')


#Fatiando Strings
urlBase=url[:interrogacao] #Se nao colocar nada no inicio, ele entende que começa do inicio
print(urlBase)

urlParametros=url[interrogacao+1:]  #Se nao colocar nada no final, ele entende que precisa percorrer tudo
print(urlParametros)

# Busca o valor de um parâmetro
parametro_busca = 'quantidade'
indice_parametro = urlParametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = urlParametros.find('&', indice_valor)
if indice_e_comercial == -1:
    valor = urlParametros[indice_valor:]
else:
    valor = urlParametros[indice_valor:indice_e_comercial]

print(valor)