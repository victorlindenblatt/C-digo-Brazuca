#gerencie um jogador de futebol lendo o nome e quantas partidas ele jogou. Depois, leia a quantidade de gols feitas
#em cada partida. Coloque tudo num diconário incluindo o total de gols durante o período.

jogadores = []

jogador = {}
while True:
    jogador["nome"] = input("Qual nome do jogador: ")
    jogador["partidas"] = float(input("Quantas partidas: "))
    jogador["Gols"] = float(input("Média de gols por partida?: "))
    jogadores.append(jogador)
    print(jogador)
    #print([1]*[2])