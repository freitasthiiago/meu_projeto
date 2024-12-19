#Crie uma classe Funcionario com atributos cod, nome e salario. Atenção às regras de negócio:

#O salário é um atributo privado, mas deve ser informado no momento de criação da instância.
#Um método exibir_informacoes() deve imprimir os dados do funcionário (nome, cod, salario atual) e o histórico de aumentos.

class Funcionario:

    def __init__(self, cod, nome, salario_inicial):
        self.cod = cod
        self.nome =  nome
        self.__salario = salario_inicial if salario_inicial > 0 else 0
        self.historico_salario =[salario_inicial]
        self.percentual = [0]
       
    #Quando o salário for alterado, não é possível definir um valor menor que o salário atual;
    #Implemente o método aumentar_salario(percentual) que aumenta o salário do funcionário com base em uma porcentagem fornecida;
    #A classe deve manter um histórico dos aumentos aplicados em uma lista. Cada aumento deve ser armazenado com o percentual aplicado e o novo salário após o aumento.
   
    def aumentar_salario(self, percentual):
        if percentual <= 0:
            print('Percentual invalido')
        
        else: 
            self.__salario = self.__salario + (self.__salario * percentual/100)
            self.historico_salario.append(self.__salario)
            self.percentual.append(percentual)
            
    
    #Um método exibir_informacoes() deve imprimir os dados do funcionário (nome, cod, salario atual) e o histórico de aumentos.
    
    def exibir_informacoes(self):
        print(f'-----------------------------\nNOME: {self.nome}\nCOD: {self.cod}\nSALARIO ATUAL: R$ {self.__salario:.2f}\n-----------------------------\n**HISTORICO DO SALARIO**')
    
        for n in self.historico_salario:
            print(f'R$ {n:.2f} - ({self.percentual[self.historico_salario.index(n)]:.1f} %)')

        print('-----------------------------')
            

func1 = Funcionario(1, 'Thiago', 2000.0)

func1.aumentar_salario(10)
print(func1.historico_salario)


func1.aumentar_salario(12.5)
print(func1.historico_salario)

   #self.__historico_aumentos.append({"percentual": percentual, "novo_salario": novo_salario})


func1.aumentar_salario(-30.5)
print(func1.historico_salario)


func1.exibir_informacoes()