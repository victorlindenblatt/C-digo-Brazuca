#Crie uma função chamada "read_file" que recebe o nome de um arquivo e tenta abri-lo para leitura.
#Se o arquivo não existir, capture a exceção 'FileNotFoundError e imprima uma mensagem amigável para o usuário.

def read_file():
    try:
        print(open(input("Nome do arquivo: ")).read())
    except FileNotFoundError:
        print("O arquivo não foi encontrado no computador")
#C:/Users/codigobrazuca/Documents/Victor python/Softskills Victor.txt
read_file()