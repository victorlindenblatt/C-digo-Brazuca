#Monte um código para dizer se o número informado é primo

for n in (0,10000):
    n = int(input("Digite um número entre 0 e 10.000: "))
    if n % 2 == 0:
        print("O número é divisivel")
    elif n % 3 == 0:
        print("O número é divisivel")
    elif n % 4 == 0:
        print("O número é divisivel")
    elif n % 5 == 0:
        print("O número é divisivel")
    elif n % 10 == 0:
        print("O número é divisivel")
    else:
        print("O número é primo")
    
     