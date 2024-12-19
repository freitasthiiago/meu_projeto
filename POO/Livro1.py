class Livro:

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.preco = 0

    def set_preco(self, preco):
        if preco < 0:
            print('Preço invalido')
        else:
            self.preco = preco
    
    def exibir_info(self):
        print(f'O livro {self.titulo} do autor {self.autor} - R$ {self.preco:.2f}')

Livro4 = Livro('O Simbolo Secreto', 'Dan Brown')
Livro4.preco = 30

Livro1 = Livro('O pacto', 'Joe Hill')
Livro2 = Livro('Anjo caído', 'Daniel Silva')
Livro3 = Livro('A farsa', 'Christopher Reich')
Livro1.preco = 19.9
Livro2.preco = 15
Livro3.preco = 45

Livro2.exibir_info()