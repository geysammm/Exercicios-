def somar_valores(*valores):
    soma = sum(valores)
    return soma
resultado = somar_valores(1, 2, 3, 4, 5)
print('A soma dos valores é:', resultado)