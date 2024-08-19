class Produto:
    def __init__(self, nome, preco, quantidade, codigo):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.codigo = codigo

    def calcular_total(self):
        total = self.preco * self.quantidade
        print(f"Total do estoque de {self.nome}: R${total:.2f}")
        return total

    def atualizar_preco(self, novo_preco):
        if novo_preco >= 0:
            self.preco = novo_preco
            print(f"Preço do produto {self.nome} atualizado para R${self.preco:.2f}")
        else:
            print("O preço não pode ser negativo!")

    def verificar_disponibilidade(self):
        if self.quantidade > 0:
            print(f"Produto {self.nome} está disponível. Quantidade em estoque: {self.quantidade}")
            return True
        else:
            print(f"Produto {self.nome} está fora de estoque.")
            return False

# Exemplo de uso da classe Produto
produto1 = Produto("Camiseta", 49.90, 20, "C001")
produto2 = Produto("Calça", 89.90, 0, "C002")

# Calculando total do estoque
produto1.calcular_total()
produto2.calcular_total()

# Atualizando o preço
produto1.atualizar_preco(54.90)

# Verificando disponibilidade
produto1.verificar_disponibilidade()
produto2.verificar_disponibilidade()