# Aarian Dhanani
# October 22nd, 2020
# Treasure hunt game

import random

rows, cols = (5, 5)

arr = [[0 for i in range(cols)] for j in range(rows)]

x1 = random.randint(0, 4)
y1 = random.randint(0, 4)

x2 = random.randint(0, 4)
y2 = random.randint(0, 4)

x3 = random.randint(0, 4)
y3 = random.randint(0, 4)

x4 = random.randint(0, 4)
y4 = random.randint(0, 4)

guess1 = 5
guess2 = 5

print("Welcome to Treasure Hunt!")

# arr[x1][y1] = 1
# arr[x2][y2] = 1
# arr[x3][y3] = 1
# arr[x4][y4] = 1

answer = "0"
check = 0
correct1 = 0
correct2 = 0
correct3 = 0
correct4 = 0

guesses = 10

while correct1 == 0 or correct2 == 0 or correct3 == 0 or correct4 == 0:

    if guesses == 0:
        print("You lose!")
        exit()

    answer = "0"
    check = 0
    
    for row in arr:
        print(row)

    while check == 0:
        while len(answer) != 2:
            answer = input("Guess a coordinate: ")
            if len(answer) != 2:
                print("Invalid input!")

        try:
            guess1 = int(answer[0])
            guess2 = int(answer[1])
            check = 1
        except ValueError:
            print("Invalid input!")
            answer = "0"

    if guess1 == x1 and guess2 == y1:
        arr[x1][y1] = 1
        print("Correct!")
        correct1 = 1
    if guess1 == x2 and guess2 == y2:
        arr[x2][y2] = 1
        print("Correct!")
        correct2 = 1
    if guess1 == x3 and guess2 == y3:
        arr[x3][y3] = 1
        print("Correct!")
        correct3 = 1
    if guess1 == x4 and guess2 == y4:
        arr[x4][y4] = 1
        print("Correct!")
        correct4 = 1

    guesses = guesses - 1

    print("You have", guesses, "guesses left!")

for row in arr:
    print(row)
print("You win!")
# Sources:
# https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/
# https://www.w3schools.com/python/ref_random_randint.asp
# https://codippa.com/check-if-string-is-integer-in-python/
# https://www.geeksforgeeks.org/python-exit-commands-quit-exit-sys-exit-and-os-_exit/

