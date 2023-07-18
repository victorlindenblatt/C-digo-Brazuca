#faça um programa que leia o nome de 4 alunos e escreva na tela o nome do escolhido para apagar o quadro
import random

Aluno1 = str(input("Nome do primeiro aluno: "))
Aluno2 = str(input("Nome do segundo aluno: "))
Aluno3 = str(input("Nome do terceiro aluno: "))
Aluno4 = str(input("Nome do quarto aluno: "))

sorteio = [Aluno1, Aluno2, Aluno3, Aluno4]

print(f"Quem vai apagar o quadro é o {sorteio[random.randrange(len(sorteio))]}")