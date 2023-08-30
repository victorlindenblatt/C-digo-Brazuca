#Defina uma classe Car com atributos make, model e year. Crie um método start_engine que imprime uma mensagem 
#indicando que o motor foi iniciado.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        self.make = input("Car make: ")
        self.model = input("Car model: ")
        self.year = input("Car year: ")
        print(f"Car make: {self.make}, Car Model:{self.model}, year:{self.year}")
        driver = input("You start the car now?(Y/N)")
        if driver == "Y":
            print("Car engine is running")
        else:
            print("Car engine is off")

car1 = Car("Audi", "Q3",2020)
car1.start_engine()