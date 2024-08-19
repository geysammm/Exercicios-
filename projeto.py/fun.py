import sys

# Dicionário para armazenar informações dos hóspedes
hospedes = {}

def cadastrar_hospede(nome, quarto, estadia):
    """Cadastra um novo hóspede."""
    hospedes[nome] = {'Quarto': quarto, 'Estadia': estadia}
    print(f"Hóspede {nome} cadastrado com sucesso!")

def buscar_hospede(nome):
    """Busca informações de um hóspede pelo nome."""
    if nome in hospedes:
        return hospedes[nome]
    else:
        return None

def listar_hospedes():
    """Lista todos os hóspedes cadastrados."""
    if hospedes:
        for nome, info in hospedes.items():
            print(f"Nome: {nome}, Quarto: {info['Quarto']}, Estadia: {info['Estadia']} dias")
    else:
        print("Nenhum hóspede cadastrado.")

def remover_hospede(nome):
    """Remove um hóspede pelo nome."""
    if nome in hospedes:
        del hospedes[nome]
        print(f"Hóspede {nome} removido com sucesso!")
    else:
        print(f"Hóspede {nome} não encontrado.")

def menu():
    """Exibe o menu de opções para o usuário."""
    while True:
        print("\n----- Sistema de Gestão do Hotel -----")
        print("1. Cadastrar Hóspede")
        print("2. Buscar Hóspede")
        print("3. Listar Hóspedes")
        print("4. Remover Hóspede")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do hóspede: ")
            quarto = input("Número do quarto: ")
            estadia = int(input("Número de dias de estadia: "))
            cadastrar_hospede(nome, quarto, estadia)
        
        elif opcao == '2':
            nome = input("Nome do hóspede: ")
            hospede = buscar_hospede(nome)
            if hospede:
                print(f"Nome: {nome}, Quarto: {hospede['Quarto']}, Estadia: {hospede['Estadia']} dias")
            else:
                print(f"Hóspede {nome} não encontrado.")
        
        elif opcao == '3':
            listar_hospedes()
        
        elif opcao == '4':
            nome = input("Nome do hóspede: ")
            remover_hospede(nome)
        
        elif opcao == '5':
            print("Saindo do sistema...")
            sys.exit()
        
        else:
            print("Opção inválida! Tente novamente.")

# Inicia o programa exibindo o menu
menu()
