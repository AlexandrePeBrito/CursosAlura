import random as rd
def iniciandoGame():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def carregandoPalavraSecreta():
    arquivo = open('D:\Meus Documentos\Documentos\GitHub\Alura\python\pythonPart2\JogoDaForca/frutas.txt','r')
    palavras=[]
    for linha in arquivo:
        linha=linha.strip().upper()
        palavras.append(linha)
    arquivo.close()
    
    num=rd.randrange(0,len(palavras))
    palavraSecreta=palavras[num]
    return palavraSecreta

def letraAcertadasInic(palavra):
    lista=['_' for i in palavra]
    return lista

def pede_chute():
    chute=input('Qual letra deseja marcar? ')
    return chute.strip().upper()

def marca_chute(palavraSecreta,letrasAcertadas,chute):
    index = 0
    for letra in palavraSecreta:
        if(letra==chute):
             letrasAcertadas[index]=letra
        index += 1

def jogar():
    iniciandoGame()
    palavraSecreta=carregandoPalavraSecreta()
    letrasAcertadas= letraAcertadasInic(palavraSecreta)
    print(letrasAcertadas)

    erros=0
    enforcou=False
    acertou=False

    
    #Enquanto nao se enforca e nem acerta -> not False == True
    while(not enforcou and not acertou ):
        chute = pede_chute()
        
        if(chute in palavraSecreta):
            marca_chute(palavraSecreta,letrasAcertadas,chute)
        else:
            erros += 1
            
        enforcou= erros==len(palavraSecreta)
        acertou= '_'not in letrasAcertadas
        print(letrasAcertadas)
    if(acertou):
        print('Parabens!!! Você Ganhou')    
    else:
        print('Que Pena, Você Perdeu!!!')

if(__name__ == "__main__"):
    jogar()
