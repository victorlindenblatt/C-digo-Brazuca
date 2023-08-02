#Escreva um programa que peça ao usuário para digitar um número inteiro e, em seguida, imprima o dobro desse número
#utilize try/except para lidar com a possibilidade de o usuário inserir um valor não numérico.

def main():
    x = get_int("Qual o número? ")
    print(f"O dobro é {x*2}")
    


def get_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Escreva um número inteiro")
        

main()