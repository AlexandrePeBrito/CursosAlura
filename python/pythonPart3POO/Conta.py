class Conta:
    #Construtor
    def __init__(self,numero,titular,saldo,limite) -> None:
        self.__numero=numero
        self.__titular=titular
        self.__saldo=saldo      #encapsulamento
        self.__limite=limite

    #Metodos
    
    def extrato(self):
        print(f'Saldo: {self.__saldo}\nTitular: {self.__titular}')
    
    def depositar(self,valor):
        self.__saldo+=valor
    
    def saque(self,valor):
        self.__saldo-=valor   
        
    #GETTERS SETTERS
    def get_limite(self):
        return self.__limite
    def set_limite(self,limite):
        self.__limite=limite