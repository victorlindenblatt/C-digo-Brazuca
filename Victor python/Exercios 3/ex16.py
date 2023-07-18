# ex16: Leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa
import math

oposto = float(input("Escreva o cateto oposto: "))
adjacente = float(input("Escreva o cateto adjacente: "))

comprimento = math.hypot(oposto , adjacente)

print((f"O comprimento da hipotenusa é: {comprimento}"))