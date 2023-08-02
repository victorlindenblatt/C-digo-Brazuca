#Crie uma função chamada "divide_numbers" que recebe dois parâmetros numéricos ( a e b) e retorna a divisão de a por b.
#Utilize try/except para tratar a divisão por zero.


def divide_numbers():
    while True:
        try:
            a = int(input("Qual é o número A: "))
            b = int(input("Qual é o número B: "))
            return a/b
        except ZeroDivisionError:
            print("Digite um número válido")
        

print(divide_numbers())