import time
    
def fatorial(n):
     f = 1
    for c in range(1, n+1):
        f *= c
        print(f"F: {f}\nC: {c}")
        time.sleep(1)
    return f

def dobro(n):
    return n*2

def triplo(n):
    return n*3

    fat = fatorial(5)
    print(fat)