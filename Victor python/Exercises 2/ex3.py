#Faça um programa que leia o preço de um produto e retorne
#o seu preço com 5% de desconto

preço = float(input("Qual é o preço do produto? "))
desconto = {preço - (preço * 0.05)}

print(f"O preço do produto com desconto é: {preço - (preço * 0.05)}")