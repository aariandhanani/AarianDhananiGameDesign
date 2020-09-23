userInput = int(input("Please input the number of terms you would like in the fibonacci."))

for x in range(5):
    for y in range(1,6 - x):
        print((6-x) - y, end = " ")
    print()

print()
