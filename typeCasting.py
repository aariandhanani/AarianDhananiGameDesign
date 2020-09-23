userInput = int(input("Please input a number.\n"))

for x in range(userInput):
    for y in range(1,(userInput + 1) - x):
        print(((userInput + 1) - x) - y, end = " ")
    print()

print()
