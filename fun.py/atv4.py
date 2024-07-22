
def real_para_dolar(valor):
    taxa_dolar = 0.18
    valor_convertido = valor * taxa_dolar
    return valor_convertido

def real_para_euro(valor):
    taxa_euro = 0.16
    valor_convertido = valor * taxa_euro
    return valor_convertido

def real_para_peso_argentino(valor):
    taxa_peso = 0.0061
    valor_convertido = valor * taxa_peso
    return valor_convertido

# Solicitando os valores ao usuário
valor_em_real = float(input('Digite o valor em reais a ser convertido: '))
pais_destino = input('Digite o nome do país para o qual deseja converter (Estados Unidos, Portugal ou Argentina): ')

# Realizando a conversão com base no país escolhido
if pais_destino.lower() == 'estados unidos':
    valor_convertido = real_para_dolar(valor_em_real)
    moeda_destino = 'dólares'
elif pais_destino.lower() == 'portugal':
    valor_convertido = real_para_euro(valor_em_real)
    moeda_destino = 'euros'
elif pais_destino.lower() == 'argentina':
    valor_convertido = real_para_peso_argentino(valor_em_real)
    moeda_destino = 'pesos argentinos'
else:
    print('País não suportado para conversão.')

# Exibindo o resultado na tela
if 'valor_convertido' in locals():
    print(f'O valor convertido de R${valor_em_real:.2f} para {pais_destino.capitalize()} é de {valor_convertido:.2f} {moeda_destino}.')
