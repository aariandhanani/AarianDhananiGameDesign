#Aarian Dhanani
#9/18/20


# 1.- Print the following pattern using for loop
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

for x in range(5):
    for y in range(1,6 - x):
        print((6-x) - y, end = " ")
    print()

print()

#Solution from class:
# begin = 5
# lines = begin
#
# for line in range (lines):
#     for number in range(begin-line, 0, -1):
#         print(number, end=" ")
#     print()
#
#
# print()


# 2. Python program to display all the prime numbers within a range
# I looked up if there's an or operator in python
number1 = 25
number2 = 50

for theNumber in range(number1,number2 + 1):
    if theNumber % 2 == 0 or theNumber % 3 == 0 or theNumber % 5 == 0 or theNumber % 7 == 0 or theNumber % 11 == 0 or theNumber % 13 == 0 or theNumber % 17 == 0 or theNumber % 19 == 0:
        print("", end = "")
    else:
        print(theNumber)


print()


# Display Fibonacci series up to 10 terms
# Expected output:
#
# Fibonacci sequence:
# 0  1  1  2  3  5  8  13  21  34

first = 0
second = 1
third = 1
numberOfTerms = 10;

for fibonacci1 in range(numberOfTerms):
    print(first, end = " ")
    third = first + second
    first = second
    second = third
