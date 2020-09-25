#Aarian Dhanani
#Functions

def testing_Functions(number):
    for x in range(number):
        for y in range(1,(number + 1) - x):
            print(((number + 1) - x) - y, end = " ")
        print()

    print()

def running_Loops():
    for x in range(1, 10):
        for z in range(9 - x):
            print(" ", end = "")
        for y in range(x):
            print(x, end = "")
        print(" ", end = "")
        for y in range(x):
            print(x, end = "")
        print("")

number = 10

for x in range(3):
    testing_Functions(number)

running_Loops()
