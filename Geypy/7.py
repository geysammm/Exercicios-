"""Estrutura condicional com operadores lógicos:
7. Para votar, você deve ter entre 18 anos e menos de 65 anos. Escreva um
@programa que pergunte sua idade e diga se você é obrigado a votar ou não."""

idade = int(input("Digite sua idade: "))

# Verificando se a pessoa é obrigada a votar
if 18 <= idade < 65:
    print("Você é obrigado(a) a votar.")
else:
    print("Você não é obrigado(a) a votar.")
    