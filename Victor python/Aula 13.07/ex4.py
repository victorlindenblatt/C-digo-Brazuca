#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço
#militar , se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# seu programa também deverá mostrar o tempop que falta ou que passou do prazo.

idade = float(input("Escreva o ano de seu nascimento: "))

if 2023 - idade == 18:
    print("Você precisa se alistar esse ano")
elif 2023 - idade > 18:
    print(f"Passou do tempo, Já tem {(2023 - idade) - 18} anos que você precisou se alistar")
else:
    print(f"Você ainda vai se alistar, falta { 18 - (2023 - idade)} anos")