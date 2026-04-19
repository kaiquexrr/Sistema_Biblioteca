class Livro:
    def __init__(self,titulo,autor,ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano


class  Usuarios:
    def __init__(self,nome,email,senha):
        self.nome = nome
        self.__email = email
        self.__senha = senha

    def get__email(self):
        return self.__email

    def set__email(self,email):
        self.__email = email

    def get__senha(self):
        return self.__senha
    
    def set__senha(self,senha):
        self.__senha = senha
    
    def pegar_livro(self,livro):
        print(f'{self.nome} pegou o livro {livro.titulo} do autor {livro.autor} publicado em {livro.ano}')


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

        
        



livro1 = Livro('O Senhor dos Anéis','J.R.R. Tolkien',1954)
usuario1 = Usuarios('João','joao@email.com','123456')

biblioteca1 = biblioteca('Biblioteca Central')
biblioteca1.livros.append(livro1)
biblioteca1.usuarios.append(usuario1)

biblioteca1.resumo_geral()
biblioteca1.pegar_livro(usuario1,livro1)
biblioteca1.emprestimo_livro(usuario1,livro1,7)
biblioteca1.devolver_livro(usuario1,livro1)