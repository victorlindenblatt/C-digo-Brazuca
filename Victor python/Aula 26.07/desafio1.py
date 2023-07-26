#Faça o exercício acima aceitar vários jogadores, inclua um sistema para visualizar detalhes do aproveitamento de cada jogador.

jogadores = []

jogador = {}
while True:
    jogador["nome"] = input("Qual nome do jogador: ")
    jogador["partidas"] = int(input("Quantas partidas: "))
    jogadores.append(jogador)
    print(jogador)