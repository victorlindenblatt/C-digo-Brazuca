#Crie um dicionário que guarde o nome, ano de nascimento, a idade e o ano de contratação e o salário de um funcionário.
#Calcule e acrescente no dicionário quantos anos a pessoa se aposentará.

funcionario = {}
funcionario["nome"] = input("Qual o seu nome: ")
funcionario["nascimento"] = nascimento = int(input("Ano de nascimento: "))
funcionario["idade"] = idade = 2023 - nascimento
funcionario["contratacao"] = input("Ano de contratação: ")
funcionario["salario"] = input("Qual o seu salário?: ")

if idade < 65:
    funcionario["tempo até aposentar"] = 65 - idade
else:
    print("Você já se aposentou")

print(funcionario)