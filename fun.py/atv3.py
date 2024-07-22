"""Faça um programa que receba três números do usuário, e identifique o maior
através de uma função e o menor número através de outra função."""

def encontrar_maior_numero(num1, num2, num3):
    return max(num1, num2, num3)

def encontrar_menor_numero(num1, num2, num3):
    return min(num1, num2, num3)

# Solicitando os números ao usuário
numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))
numero3 = float(input('Digite o terceiro número: '))

# Encontrando o maior e o menor número
maior_numero = encontrar_maior_numero(numero1, numero2, numero3)
menor_numero = encontrar_menor_numero(numero1, numero2, numero3)

# Exibindo os resultados na tela
print(f'O maior número é: {maior_numero}')
print(f'O menor número é: {menor_numero}')

