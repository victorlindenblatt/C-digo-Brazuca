# Crie um programa que receba 5 valores int e no final mostre a soma apenas dos pares
soma = 0

for i in range(1, 6):
    n = int(input("Digite o número: "))
    if n % 2 == 0:
        soma += n 
print(soma)
