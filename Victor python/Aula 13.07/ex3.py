# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# o primeiro valor é maior
# o segundo valor é maior
# Não existe valor maior, os dois são iguais

num1 = int(input("Escreva o primeiro número: "))
num2 = int(input("Escreva o segundo número: "))

if num1 > num2:
    print("O primeiro valor é maior")
else:
    print("O segundo valor é maior")