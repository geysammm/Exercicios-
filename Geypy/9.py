"""Estruturas de repetição:
9. Faça um programa que leia um nome de usuário e a sua senha e não aceite
a senha igual ao nome do usuário, mostrando uma mensagem de erro e
voltando a pedir as informações."""

while True:
    # Pedindo ao usuário para digitar o nome de usuário e a senha
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    # Verificando se a senha é igual ao nome de usuário
    if senha != usuario:
        print("Cadastro realizado com sucesso!")
        break
    else:
        print("Erro: A senha não pode ser igual ao nome de usuário. Por favor, tente novamente.")
