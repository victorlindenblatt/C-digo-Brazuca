#def msg(m):
    #print("-"*30)
    #print(m)
    #print("-"*30)

#if __name__=="__main__":
    #msg("Victor")
    #msg("Estudar mais")
    #msg("Resiliênia")
    #msg("Bora")

#def test():
    #return "Victor","Fazolato"

#var = test()
#print(var)

#def test(*args):
    #for i in args:
        #print(i)

#test(1, 2, 3, 4, "CB", 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, "transfero", 21)

#lista = [1, 2, 3, 4, 5]

#n1, n2, n3, *n = lista
#print(n)
#print(n3)
#print(lista)

def test(*args):
    print(args)
    

lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
test(*lista, *lista2)

def test(*args, **kwargs):
    print(args)
    print(kwargs["nome"], kwargs["idade"])
    idade = kwargs.get("idade")  #  ---> melhor método para fazer um kwargs

lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
test(*lista, *lista2, nome="victor", idade="22")