import pandas as pd 

dadosJson=pd.read_json('D:/Meus Documentos/Documentos/GitHub/CursosAlura/PythonDataScience/tratandoDados/importando/aluguel.json')
#print(dadosJson)

dadosTxt=pd.read_table('D:/Meus Documentos/Documentos/GitHub/CursosAlura/PythonDataScience/tratandoDados/importando/aluguel.txt')
#print(dadosTxt)

dadosExcel=pd.read_excel('D:/Meus Documentos/Documentos/GitHub/CursosAlura/PythonDataScience/tratandoDados/importando/aluguel.xlsx')
#print(dadosExcel)

dadosHtml=pd.read_html('D:/Meus Documentos/Documentos/GitHub/CursosAlura/PythonDataScience/tratandoDados/importando/dados_html_1.html')
#print(dadosHtml)

dadosHtml2=pd.read_html('D:/Meus Documentos/Documentos/GitHub/CursosAlura/PythonDataScience/tratandoDados/importando/dados_html_2.html')
#print(dadosHtml2)
print(dadosHtml2[1])
print(dadosHtml2[2])
