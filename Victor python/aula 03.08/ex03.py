#Crie uma classe chamada "Aluno" que possua o método __init__ para inicializar as propriedades "nome" e "nota" do aluno.
#Em seguida, crie dois objetos da classe "Aluno" e verifique qual dos dos dois obteve a maior nota.


# a minha forma que eu resolvi o 

class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota


def main():
    aluno1 = get_aluno1()
    aluno2 = get_aluno2()
    if aluno1.nota > aluno2.nota:
        print(f"A nota do  {aluno1.nome} é maior que a nota do {aluno2.nome}")
    elif aluno1.nota < aluno2.nota:
        print(f"A nota do  {aluno2.nome} é maior que a nota do {aluno1.nome}")
    else:
        print(f"A nota do  {aluno1.nome} e a nota do {aluno2.nome} é a mesma")


def get_aluno1():
    nome = input("Nome: ")
    nota = float(input("Nota: "))
    try:
        return Aluno(nome, nota)
    except ValueError:
        ...

def get_aluno2():
    nome = input("Nome: ")
    nota = float(input("Nota: "))
    try:
        return Aluno(nome, nota)
    except ValueError:
        ...


if __name__ == "__main__":
    main()