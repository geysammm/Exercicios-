"""Faça um Programa que peça uma data no formato dd/mm/aaaa e determine
se a mesma é uma data válida."""

#Pedindo ao usuário para digitar uma data
data = input("Digite uma data no formato dd/mm/aaaa: ")

# Separando o dia, mês e ano
dia, mes, ano = data.split('/')

# Verificando se a data é válida
from datetime import datetime
data_valida = True
try:
    datetime(int(ano), int(mes), int(dia))
except ValueError:
    data_valida = False

# Imprimindo o resultado
if data_valida:
    print("A data é válida.")
else:
    print("A data é inválida.")

