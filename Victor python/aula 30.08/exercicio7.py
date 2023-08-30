#7Crie uma classe Employee com atributos name, position e salary. Adicione um método apply_raise que aumenta o salário do 
#funcionário em uma determinada porcentagem.

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def apply_raise(self):
        self.name = input("What your name? ")
        self.position = input("What is your position? ")
        self.salary = float(input("What is your salary? "))
        print(f"Hi, {self.name}, your salary increase 5%, now is: {self.salary * 1.05}")

employee1 = Employee(0,0,0)
employee1.apply_raise()