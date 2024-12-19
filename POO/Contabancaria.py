class ContaBancaria:

    def __init__(self, titular, saldo):
        self.titular=titular
        self.saldo=saldo
            
    def depositar(self, valor):
        self.saldo = self.saldo + valor
       
    
    def sacar(self, saldo, valor):
        if saldo - valor <0:
            print('Saldo Insuficiente')
        else:
            self.saldo = self.saldo - valor
    
    def exibir_saldo(self):
        print(f'Saldo atual: R$ {self.saldo:.2f}')
    
    def exibir_info(self):
        print(f'Titular: {self.titular}n/Saldo: {self.saldo:.2f}')

titular = str(input('Insira o Nome do titular: '))
saldo = float(input('Insira o primeiro valor: '))

cliente1 = ContaBancaria(titular, saldo)

cliente1.exibir_info()

valor = float(input('Informe um valor: '))