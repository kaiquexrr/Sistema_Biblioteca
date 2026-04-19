from livros import Livro
from usuario import Usuarios
from biblioteca import biblioteca

livro1 = Livro('O Senhor dos Anéis','J.R.R. Tolkien',1954)
usuario1 = Usuarios('João','joao@email.com','123456')

biblioteca1 = biblioteca('Biblioteca Central')
biblioteca1.livros.append(livro1)
biblioteca1.usuarios.append(usuario1)

biblioteca1.resumo_geral()
biblioteca1.pegar_livro(usuario1,livro1)
biblioteca1.emprestimo_livro(usuario1,livro1,7)
biblioteca1.devolver_livro(usuario1,livro1)