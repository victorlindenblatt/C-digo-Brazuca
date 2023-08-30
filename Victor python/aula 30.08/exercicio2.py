#Defina uma classe BankAccount com atributos privados balance e account_number. Crie métodos deposit e withdraw para manipular o saldo.

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self):
        operation1 = float(input("What values you want deposit?" ))
        print(f"You deposit {operation1} $ in your account {self.__account_number}, updated account balance: {self.__balance+operation1}$")
        return BankAccount

    def withdraw(self):
        operation2 = float(input("What values you want withdraw?"))
        if operation2 < self.__balance:
            self.__balance - operation2
            print(f"You withdraw {operation2} $ in your account {self.__account_number}, updated account balance: {self.__balance - operation2}$")
        else:
            print("This operation can't be realized")
        
conta1 = BankAccount(1, 3500)
conta1.deposit()
conta1.withdraw()