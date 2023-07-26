lista = list()
dicionarios = dict()

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
dobra = []


#CRIAÇÃO DE LISTA

#for n in lista:
    #dobra.append(n/2)
#print(dobra)

#contato = {}

#contato["nome"] = "Victor"
#print(contato)

#jogadores = []

#jogador = {}
#while True:
    #jogador["nome"] = input("Qual nome do jogador: ")
    #jogador["partidas"] = int(input("Quantas partidas: "))
    #jogadores.append(jogador)


#outra maneira de fazer o primeiro código
#teste

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
dobra = [n*2 for n in lista]
print(dobra)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
dobra = [n for n in lista if n % 2 == 0]
dobra = [n if n % 2 == 0 else None for n in lista]
print(dobra)

nomes = ["Rodrigo", "Pedro", "Antonio"]
lista_modificada = [nome for nome in nomes]
print(lista_modificada)

lista = [
    ("chave", "valor"),
    ("Chave 2", "valor2")
]
print(type(lista[0]))
d1 = {k: v for k, v in lista}
print(d1, type(d1))


filme1 = {"Nome": "Vingadores", "ano": 2013}
filme2 = {"Nome": "Spider Man", "ano": 2015}
filme3 = {"Nome": "Mercenários", "ano": 2033}
locadora = [filme1, filme2, filme3]

print(locadora[2]["ano"])

#um dicionario funciona com 2 objetos, chave e o valor, que forma um item.