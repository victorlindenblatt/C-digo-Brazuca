print("Start")

if True:
    print("É verdade")

print("É")

print("Start")

if False:
    print("É verdade")

print("É")

name = input("Say your name: ")

if name == "Victor" or name == "Gabriel" or name == "Michael":
    print("Nice to meet you")
elif name == "Pedro":
    print("You are good")
else:
    print("You don't study here")

print(f"Hello, {name}")

score = int(input("Whats score: "))

if score >= 9 and score < 10:
    print("You get an A")
elif score >= 7 and score < 9:
    print("You get an A")
elif score >= 5 and score < 7:
    print("You get an A")
elif score >= 4 and score < 5:
    print("You get an A")
else:
    print("You get an F")