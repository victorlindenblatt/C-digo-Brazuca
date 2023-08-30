#Defina uma classe TemperatureConverter com métodos para converter de Celsius para Fahrenheit e vice-versa. 
#Mantenha os atributos e métodos privados.

class TemperatureConverter:
    def __init__(self,temperatura, nome):
        self.temperatura = temperatura
        self.nome = nome

    def main(self):
        conta = int(input(f"{1}- Convert in celsius \n{2}- Convert in fahrenheit\n Resposta: "))
        if conta == 1:
            self.celsius()
        elif conta == 2:
            self.fahrenheit()
        else:
            print("Escolha uma operação válida")

    def celsius():

    def fahrenheit():        
