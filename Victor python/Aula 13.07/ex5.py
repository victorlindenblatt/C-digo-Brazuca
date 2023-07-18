#Crie um programa que leia duas notas de um aluno e calcule sua média,
#mostrando uma mensagem no final, de acordo com a média atingida:
# média abaixo de 5.0: reprovado
# média entre 5.0 e 6.9: Recuperação
# Média 7.0 ou superior: aprovado

nota1 = float(input("Escreva sua nota da VAE 1: "))
nota2 = float(input("Escreva sua nota da VAE 2: "))

media = (nota1 + nota2) / 2

if media < 5:
    print("Reprovado!")
elif media < 7:
    print("Você está de recuperação")
else:
    print("Você está aprovado!")
