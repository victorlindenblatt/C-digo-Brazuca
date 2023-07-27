#Crie uma função que receba uma lista de números como entrada
#e retorne o maior número presente na lista.

def compare(*args):
    maior = args[0]
    for x in range(0,len(args)):
        if args [x] > maior:
            maior = args[x]
    return maior

lista = compare(2,1,5,15,10,11,13,9)
print(f"O maior número é",lista)
