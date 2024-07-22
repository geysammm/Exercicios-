"""Escreva um programa que possa cadastrar clientes ou funcionários para uma
loja. Se o usuário quiser cadastrar um cliente, dados de nome, endereço,
CPF devem ser solicitados. Caso o usuário prefira adicionar um novo
funcionário, dados de nome, salário, cargo e CPF devem ser requisitados.
Utilize comandos de manipulação de string para personalizar a saída."""

def cadastrar_cliente():
    nome = input('Digite o nome do cliente: ')
    endereco = input('Digite o endereço do cliente: ')
    cpf = input('Digite o CPF do cliente: ')
    return f'Cliente cadastrado - Nome: {nome}, Endereço: {endereco}, CPF: {cpf}'

def cadastrar_funcionario():
    nome = input('Digite o nome do funcionário: ')
    salario = input('Digite o salário do funcionário: ')
    cargo = input('Digite o cargo do funcionário: ')
    cpf = input('Digite o CPF do funcionário: ')
    return f'Funcionário cadastrado - Nome: {nome}, Salário: {salario}, Cargo: {cargo}, CPF: {cpf}'

# Menu de opções
opcao = input('Deseja cadastrar um cliente (C) ou um funcionário (F)? ')

if opcao.lower() == 'c':
    resultado = cadastrar_cliente()
elif opcao.lower() == 'f':
    resultado = cadastrar_funcionario()
else:
    resultado = 'Opção inválida.'

print(resultado)

