
#try:
    #x = int(input("Whats x: "))
    #print(f"X is {x}")
#except ValueError:
    #print("Digite um número inteiro")

#def main():
   #x = get_int()
    #print(f"X is {x}")


#def get_int():
    #while True:
        #try:
            #return int(input("Whats x: "))
        #except ValueError:
           #print("X invalid")
        

#main()

def main():
    x = get_int("Whats x: ")
    y = get_int("Whats y: ")
    print(f"X is {x}")
    print(f"Y is {y}")


def get_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("X invalid")
        

main()


#finaly
#palavra reservada pass