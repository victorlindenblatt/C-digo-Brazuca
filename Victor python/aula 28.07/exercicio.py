list = [1,2,3,4,5]

def soma():
    total = 0
    for num in list:
        total += num
        print(total)
    return total

soma()

def mult():
    total = 1
    for num in list:
        total *= num
        print(total)
    return total

mult()