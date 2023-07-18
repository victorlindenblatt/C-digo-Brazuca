# Faça um programa que leia a quantidade de dias e km rodados por um carro
#alugado, depois calcule o valor do contrato sabendo que:
#O dia custa 60 reais e cada km custa 15 centavos

dia = float(input("Quantos dias você ficou com o carro? "))
km = float(input("Quantos km você andou? "))

dia = dia * 60
km =  km * 0.15

preço = dia + km

print(f"Você tem que pagar {preço}")

