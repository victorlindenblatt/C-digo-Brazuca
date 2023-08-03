#Crie uma classe chamada "Retângulo" que possua o método __init__ para inicializar as propriedades "largura" e "altura"
#do retângulo. Em seguida, crie um objeto da classe "Retângulo" e calcule e imprima a área do retângulo.

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura


def main():
    retangulo = get_area()
    print(f"A área do retângulo é {retangulo.largura * retangulo.altura}")


def get_area():
    largura = int(input("Largura: "))
    altura = int(input("Altura: "))
    try:
        return Retangulo(largura,altura)
    except ValueError:
        ...


if __name__ == "__main__":
    main()