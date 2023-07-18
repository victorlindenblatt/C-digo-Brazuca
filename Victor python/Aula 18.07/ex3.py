# Desenvolva um programa que calcule a soma de todos números múltiplos de três entre 1 e 500

soma = 0
cont = 0

for i in range (1, 500):
    if i % 3 == 0:
        soma = soma + i
        cont = cont + 1
        print('Soma:', soma)
        print('Números divisiveis por 3 entre 1 e 500:', cont)