#Desenvolva uma classe Book com atributos title, author e year. Implemente um método get_age que retorna 
#quantos anos o livro tem desde o ano atual.

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author =author
        self.year = year

    def get_age(self):
        self.title = (input("Book title: "))
        self.author = (input("Book author: "))
        self.year = int(input("Book year: "))
        print(f"The book {self.title} writing by {self.author} have {2023 - self.year} years")

book_years = Book(0,0,0)
book_years.get_age()