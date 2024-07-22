"""Faça um programa que peça um número inteiro e determine se ele é ou não
um número primo. Um número primo é aquele que é divisível somente por ele
mesmo e por 1."""

# Pedindo ao usuário para digitar um número inteiro
numero = int(input("Digite um número inteiro: "))

# Verificando se o número é primo
primo = numero > 1 and all(numero % i != 0 for i in range(2, int(numero ** 0.5) + 1))

# Imprimindo o resultado
if primo:
    print(f"O número {numero} é primo.")
else:
    print(f"O número {numero} não é primo.")




