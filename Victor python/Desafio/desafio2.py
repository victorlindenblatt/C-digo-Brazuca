reta1=float(input("Informe a primeira reta: "))
reta2=float(input("Informe a segunda reta: "))
reta3=float(input("Informe a terceira reta: "))

if reta1 + reta2 < reta3 or reta1 + reta3 < reta2 or reta2 + reta3 < reta2:
    print ("Não é um triângulo!")

elif reta1 == reta2 and reta1 == reta3:
    print ("Este triangulo é Equilátero!")

elif reta1 == reta2 or reta1 == reta3:
    print ("Este triangulo é Isósceles")

else:
    print ("Este triangulo é Escaleno")