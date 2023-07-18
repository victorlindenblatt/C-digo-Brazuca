#Escreva um código que pergunte o salário de um funcionário e de um aumento de 15% caso o salário for maior que 1250, caso contrario 10%.

salario = float(input("Qual é o seu salário? "))

aumento1 = salario + salario * 0.15
aumento2 = salario + salario * 0.10

if salario >= 1250:
    print(f"O seu salário aumentou para {aumento1}")
else:
    print(f"O seu salário aumento para {aumento2}")