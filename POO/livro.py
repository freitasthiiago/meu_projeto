class livro:

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def exibir_informacoes(self):
        print(f'{self.titulo} do autor {self.autor}')

livro1 = livro('O pacto', 'Joe Hill')
livro2 = livro('Anjo caído', 'Daniel Silva')
livro3 = livro('A farsa', 'Christopher Reich')

livro1.exibir_informacoes()
livro2.exibir_informacoes()
livro3.exibir_informacoes()
