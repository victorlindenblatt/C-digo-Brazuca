#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos
#anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou o empréstimo será negado.   #Falar o número do salário e o valor máximo de crédito

casa = float(input("Qual o valor da casa? "))
salario = float(input("Qual o seu salário? "))
anos = float(input("Em quantos anos você vai pagar? "))

credito = salario * 0.30
parcela = casa / anos
parcelamensal = parcela / 12

if credito > parcelamensal:
    print(f"O seu salário é {salario} e o valor máximo do crédito é: {credito} e o valor da parcela mensal é {parcela}")
    print("Crédito aprovado")
else:
    print("Crédito negado")

