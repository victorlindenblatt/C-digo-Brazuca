#Escreva um programa que solicite ao usuário que digite seu nome e sua idade. Em seguida, tente converter a idade em um número inteiro.
#Se a conversão falhar, informe ao usuário que a idade digitada é inválida e continue o programa. 
#Caso contrário, exiba uma mensagem com o nome a idade.

def get_user():
    while True:
        try:
            nome = input("Qual o seu nome? ")
            idade = int(input("Qual a sua idade? "))
        except ValueError:
            print("Idade digitada é inválida")
        else:
            print(f"Prazer {nome}, você tem {idade} anos")
            break

get_user()