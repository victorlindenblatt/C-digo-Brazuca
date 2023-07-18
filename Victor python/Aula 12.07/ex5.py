#Faça um programa  leia 3 valores e diga o maior e o menor valor
primeiro = int(input("escolha o primeiro número: "))
segundo = int(input("escolha o segundo número: "))
terceiro = int(input("escolha o terceiro número: "))

#primeiro número

maior = primeiro
menor = primeiro

if primeiro == segundo and primeiro == terceiro:
    print("Os números são iguais")
else:
    if (segundo > maior):
     maior = segundo
    if (terceiro > maior):
     maior = terceiro

    print('O maior é: ', maior)

    if (segundo < menor):
     menor = segundo
    if (terceiro < menor):
     menor = terceiro

    print('O menor é: ', menor)