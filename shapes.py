#Aarian Dhanani

number = 15

for x in range(1, (number + 1)):
    for y in range(x):
        print("*", end = "")
    for z in range(number - x):
        print(" ", end = "")


    for y in range((number + 1) - x):
        print("*", end = "")
    for z in range(x - 1):
        print(" ", end = "")


    for z in range(x - 1):
        print(" ", end = "")
    for y in range((number + 1) - x):
        print("*", end = "")


    for z in range(number - x):
        print(" ", end = "")
    for y in range(x):
        print("*", end = "")
    print(" ", end = "")
    print("")
