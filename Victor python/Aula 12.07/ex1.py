#Crie um jogo que faça o computador pensar em um número de 0 a 5 e permita o usuário ter um chute para acertar

import random

num = int(input("Escreva um número de 1 a 5: "))

acerto = random.randint(1,5)

if num == acerto:
    print("Você ganhou!")
else:
    print("Você perdeu")

print(f"O número escolhido foi: {acerto}")