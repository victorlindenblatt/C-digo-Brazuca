#Crie um programa onde 4 jogadores jogam um dado e guarde esses resultados em um dicionário
#No final, coloque esse dicionário em ordem (1º,2º...)

import random

player1 = {"Nome": "Player1","dado": random.randint(1,6)}
player2 = {"Nome": "Player1","dado":random.randint(1,6)}
player3 = {"Nome": "Player1","dado":random.randint(1,6)}
player4 = {"Nome": "Player1","dado":random.randint(1,6)}

lista = [player1, player2, player3, player4]
for jogador in enumerate(lista):
    print(jogador)