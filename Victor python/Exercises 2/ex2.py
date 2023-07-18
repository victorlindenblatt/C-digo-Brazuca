#Faça um programa que leia a altura e largura de uma parede e calcule
#sua area, mostre quantos litros de tinta sera necessário para pintar
#sabendo que 1l pinta 2m quadrados

altura = float(input("Qual é a altura da parede em metros? "))
largura = float(input("Qual é a largura da parede em metros? "))


print(f"A área é: {altura * largura}m e você ira precisar de {(altura * largura) / 2} litros de tinta")