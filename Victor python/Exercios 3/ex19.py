import random

Aluno1 = str(input("Nome do primeiro aluno: "))
Aluno2 = str(input("Nome do segundo aluno: "))
Aluno3 = str(input("Nome do terceiro aluno: "))
Aluno4 = str(input("Nome do quarto aluno: "))

sorteio = [Aluno1, Aluno2, Aluno3, Aluno4]

random.shuffle(sorteio)

print(f"A ordem da apresentação será {sorteio}")