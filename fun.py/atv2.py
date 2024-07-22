#faça um programa que calcule a área de um terreno e imprima na tela.

def calcular_area_terreno(comprimento, largura):
    area = comprimento * largura
    return area

# Solicitando as dimensões do terreno ao usuário
comprimento_terreno = float(input('Digite o comprimento do terreno em metros: '))
largura_terreno = float(input('Digite a largura do terreno em metros: '))

# Calculando a área do terreno
area_terreno = calcular_area_terreno(comprimento_terreno, largura_terreno)

# Exibindo a área calculada na tela
print(f'A área do terreno é de {area_terreno} metros quadrados.')
