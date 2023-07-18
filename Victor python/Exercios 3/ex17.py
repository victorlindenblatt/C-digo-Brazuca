#leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

import math

angulo = float(input("Escreva o ângulo da aresta: "))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print((f"O comprimento do seno é: {seno}, o cosseno é {cosseno} e a tangente é {tangente}"))

#print(seno)
#print("seno: ""{0:.2f}".format(seno))
#print("cosseno: ""{0:.2f}".format(cosseno))
#print("tangente: ""{0:.2f}".format(tangente))