"""Para ter acesso a fila de prioridade, você deve ser idoso, gestante ou PCD.
Escreva um programa que pergunta a situação do usuário (se é idoso, se é
gestante, se é PCD ou nenhum destes) e diga se ele pode ter acesso a fila
prioridade ou não."""

situacao = input("Qual é a sua situação? (Idoso/Gestante/PCD/Nenhum): ").lower()

# Verificando se o usuário tem acesso à fila de prioridade
if situacao == 'idoso' or situacao == 'gestante' or situacao == 'pcd':
    print("Você tem acesso à fila de prioridade.")
else:
    print("Você não tem acesso à fila de prioridade.")

