
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

biblioteca1 = biblioteca('Biblioteca Central')

    



livro1 = Livro('O Senhor dos Anéis','J.R.R. Tolkien',1954)
usuario1 = Usuarios('João','joao@email.com','123456')
usuario1.pegar_livro(livro1)