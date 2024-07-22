#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra=input("Digite uma letra:").lower()
if letra in 'aeiou':
    print("vogal") 
elif letra in 'bcdfghjklmnpqrstvwxyz':
    print('consoante')
 
else:
    print("inválido")

