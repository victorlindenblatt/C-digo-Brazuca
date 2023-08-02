#Escreva um programa que leia um valor númerico inteiro do usuário e imprima o resultado da raiz quadrada desse valor.
#Utilize try/except para lidar com a possibilidade de o usuário inserir um número negativo.

#tenho que refazer

def main():
    x = get_raiz("Qual o número? ")
    print(f"A raiz quadrada de {x} é {x ** 0.5}")
    


def get_raiz(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("Escreva um número inteiro")
        

main()