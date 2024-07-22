
def converter_para_12h(hora, minuto):
    if hora == 0:
        hora_12h = 12
        periodo = 'A.M.'
    elif hora < 12:
        hora_12h = hora
        periodo = 'A.M.'
    elif hora == 12:
        hora_12h = 12
        periodo = 'P.M.'
    else:
        hora_12h = hora - 12
        periodo = 'P.M.'
    
    return hora_12h, minuto, periodo

def personalizar_saida(hora_12h, minuto, periodo):
    return f'{hora_12h}:{minuto} {periodo}'

# Entrada de dados
hora = int(input('Digite a hora (formato de 24 horas): '))
minuto = int(input('Digite os minutos: '))

# Conversão para notação de 12 horas
hora_12h, minuto, periodo = converter_para_12h(hora, minuto)

# Saída personalizada
saida = personalizar_saida(hora_12h, minuto, periodo)
print(saida)
