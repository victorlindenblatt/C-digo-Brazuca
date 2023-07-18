#Faça um programa que leia a distância em km de uma viagem, se a distância for menor ou igual a 200km cobre 50 centavos por km rodado,
#caso contrário cobre 45 centavos.

viagem = float(input("Qual foi a distância percorrida durante a viagem em km? "))

if viagem <= 200 and viagem > 0:
    print(f"O preço da viagem foi {viagem * 0.5}R$")
elif viagem > 0:
    print(f"O preço da viagem foi {viagem * 0.45}")
else:
    print("Esse valor não existe")
