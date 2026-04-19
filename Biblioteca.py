from Livros import Livro
from Usuario import Usuarios
class biblioteca:
    def __init__(self,nome):
        self.nome = nome
        self.livros = []
        self.usuarios = []

    def pegar_livro(self,usuario,livro):
        if livro in self.livros:
            usuario.pegar_livro(livro)
            print(f'o livro {livro.titulo} foi retirado da biblioteca {self.nome}')
            self.livros.remove(livro)
        else:
            print(f'o livro {livro.titulo} nao esta disponivel na biblioteca {self.nome}')
    
    def devolver_livro(self,usuario,livro):
        self.livros.append(livro)
        print(f'{usuario.nome} devolveu o livro {livro.titulo} para a biblioteca {self.nome}')


    def disponibilidade_livro(self,livro,titulo):
        if livro in self.livros:
            print(f'o livro {titulo} esta disponivel na biblioteca {self.nome}')
        else:
            print(f'o livro {titulo} nao esta disponivel na biblioteca {self.nome}')
            
    def emprestimo_livro(self,usuario,livro,tempo):
        if livro in self.livros:
            usuario.pegar_livro(livro)
            self.livros.remove(livro)
            print(f'o livro {livro.titulo} foi emprestado para {usuario.nome} por {tempo} dias na biblioteca {self.nome}')
            print(f'devolver livro {livro.titulo} para a biblioteca {self.nome} apos {tempo} dias')
        else:
            print(f'o livro {livro.titulo} nao esta disponivel para emprestimo na biblioteca {self.nome}')

    def resumo_geral(self):
        print(f'biblioteca {self.nome}')
        print('Livros disponiveis:')
        for livro in self.livros:
            print(f'- {livro.titulo} de {livro.autor} publicado em {livro.ano}')
        print('Usuarios cadastrados:') 
        for usuario in self.usuarios:
            print(f'- {usuario.nome} com email {usuario.get__email()}')
