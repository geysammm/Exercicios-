#10.Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

while True:
    # Solicitando ao usuário para inserir as informações
    nome = input("Digite seu nome (maior que 3 caracteres): ")
    idade = int(input("Digite sua idade (entre 0 e 150): "))
    salario = float(input("Digite seu salário (maior que zero): "))
    sexo = input("Digite seu sexo ('f' para feminino, 'm' para masculino): ").lower()
    estado_civil = input("Digite seu estado civil ('s' para solteiro(a), 'c' para casado(a), 'v' para viúvo(a), 'd' para divorciado(a): ").lower()

    # Validando as informações
    if len(nome) > 3 and 0 <= idade <= 150 and salario > 0 and sexo in ['f', 'm'] and estado_civil in ['s', 'c', 'v', 'd']:
        print("Cadastro realizado com sucesso!")
        break
    else:
        print("Erro: Alguma informação inserida não é válida. Por favor, verifique e tente novamente.\n")