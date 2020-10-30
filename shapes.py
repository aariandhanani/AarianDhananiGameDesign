#Aarian Dhanani

number = 9

for x in range(1, (number + 1)):
    # Prints the left section
    for y in range(x):
        print("*", end = "")
    for z in range(number - x):
        print(" ", end = "")

    # Prints the 2nd section
    for y in range((number + 1) - x):
        print("*", end = "")
    for z in range(x - 1):
        print(" ", end = "")

    # Prints the 3rd section
    for z in range(x - 1):
        print(" ", end = "")
    for y in range((number + 1) - x):
        print("*", end = "")

    # Prints the 4th section
    for z in range(number - x):
        print(" ", end = "")
    for y in range(x):
        print("*", end = "")
    print("")
