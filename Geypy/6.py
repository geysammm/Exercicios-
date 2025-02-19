#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
#As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?"
#O programa deve no final emitir uma classificação sobre a participação da
#pessoa no crime. Se a pessoa responder positivamente a 2 questões ela
#deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como
#"Assassino". Caso contrário, ele será classificado como "Inocente".

# Fazendo as perguntas e contabilizando respostas positivas
respostas_positivas = sum(input(pergunta).strip().lower() == 'sim' for pergunta in [
    "Telefonou para a vítima? ",
    "Esteve no local do crime? ",
    "Mora perto da vítima? ",
    "Devia para a vítima? ",
    "Já trabalhou com a vítima? "
])

# Emitindo a classificação
if respostas_positivas == 2:
    print("Você é considerado(a) suspeito(a) do crime.")
elif 3 <= respostas_positivas <= 4:
    print("Você é considerado(a) cúmplice do crime.")
elif respostas_positivas == 5:
    print("Você é considerado(a) o assassino.")
else:
    print("Você é considerado(a) inocente em relação ao crime.")