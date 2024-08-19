class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def exibir_detalhes(self):
        return f"Título: {self.titulo}\nAutor: {self.autor}\nAno de Publicação: {self.ano_publicacao}"

# Exemplo de uso da classe Livro
livro1 = Livro("Dom Casmurro", "Machado de Assis", 1899)
livro2 = Livro("1984", "George Orwell", 1949)

# Exibindo os detalhes dos livros
print(livro1.exibir_detalhes())
print(livro2.exibir_detalhes())