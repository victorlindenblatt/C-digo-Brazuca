#Faça um programa que leia a quilometragem de um carro, caso esteja acima dos 80km/h, multe o carro

velocidade = float(input("Qual foi a velocidade máxima do carro? "))

if velocidade <= 80:
    print("Você dirigiu corretamente, parabéns!")
else:
    print("Você ultrapassou os limites e foi multado")

