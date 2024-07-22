#Faça um programa que receba dois números inteiros e gere os números
#inteiros que estão no intervalo compreendido por eles.
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

start_num = min(num1, num2)
end_num = max(num1, num2)

print("Números no intervalo entre", start_num, "e", end_num, ":")
for i in range(start_num, end_num + 1):
    print(i)