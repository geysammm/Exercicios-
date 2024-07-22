"""Crie um programa em Python que peça dois números ao usuário. 
Em seguida, você vai mostrar a soma, subtração, multiplicação, divisão,
exponenciação e resto da divisão do primeiro número pelo segundo."""

num1 =float(input("Digite o primeiro número:"))
num2 =float(input("Digite o segundo número:"))
soma = num1+num2
subtracao = num1-num2
multiplicacao = num1*num2
divisao = num1/num2
resto_divisao =num1%num2

print("soma:",soma)
print("subtracao:",subtracao)
print("multiplicacao:",multiplicacao)
print("divisao:",divisao)
print("resto_divisao:",resto_divisao)