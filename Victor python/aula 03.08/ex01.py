#Crie uma classe chamada "Cachorro" que possua o método __init__ para inicializar as propriedades "nome" e "idade"
# do cachorro. Em seguida, crie um objeto da classe "Cachorro" e imprima o nome e a idade do cachorro.

class Cachorro:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def main():
    cachorro = get_cachorro()
    print(f"The dog name is {cachorro.name} and have {cachorro.age} years old")


def get_cachorro():
    name = input("Name: ")
    age = input("Age: ")
    try:
        return Cachorro(name, age)
    except ValueError:
        ...


if __name__ == "__main__":
    main()