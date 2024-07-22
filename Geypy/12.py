#.Faça um programa que, dado um conjunto de N números, determine o menor
#valor, o maior valor e a soma dos valores.
# Pedindo ao usuário para inserir a quantidade de números
# Pedindo ao usuário para inserir a quantidade de números

n = int(input("Insira a quantidade de números que deseja analisar: "))

# Solicitando que o usuário insira os N números
numeros = []
for i in range(n):
    num = float(input(f"Insira o {i+1}º número: "))
    numeros.append(num)
# Encontrando o menor e o maior valor
menor_valor = min(numeros)
maior_valor = max(numeros)

# Calculando a soma dos valores
soma_valores = sum(numeros)

print(f"O menor valor é: {menor_valor}")
print(f"O maior valor é: {maior_valor}")
print(f"A soma dos valores é: {soma_valores}")

