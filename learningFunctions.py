#Aarian Dhanani
#Functions

def testing_Functions(number):
    for x in range(number):
        for y in range(1,(number + 1) - x):
            print(((number + 1) - x) - y, end = " ")
        print()

    print()

number = 10

for x in range(3):
    testing_Functions(number)
