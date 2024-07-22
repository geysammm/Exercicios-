def soma(num1,num2):
    return num1+num2
def subtracao(num1,num2):
    return num1-num2
def multiplicacao(num1,num2):
    return num1*num2
def divisao(num1,num2):
    return num1/num2

def calculadora():
    num1 = int(input("Digite um numero:"))
    num2 = int(input("Digite um numero:"))
    print(f" o valor da soma de{num1} + {num2} = {soma(num1,num2)}")
    print(f" o valor da subtracao de {num1} - {num2} = {subtracao (num1,num2)}")
    print(f" o valor da multiplicacao de {num1} * {num2} = {multiplicacao (num1,num2)}")
    print(f" o valor da divisao de {num1} / {num2} = {divisao (num1,num2)}")

calculadora()

