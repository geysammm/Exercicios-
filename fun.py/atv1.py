"""
Escreva um código que receba o nome de uma pessoa e imprima uma
saudação personalizada na tela com o nome do usuário.
"""

def saudacao_personalizada(nome):
    saudacao = f'Olá, {nome}! Seja bem-vinda.'
    print(saudacao)
nome_usuario = input('Qual é o seu nome? ')
saudacao_personalizada(nome_usuario)