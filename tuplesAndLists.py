# Aarian Dhanani
# 10/5/20
# Tuples and Lists Assignment

# 1. Write a Python program to create a tuple.
tuple = ("hi", "hello")

# 2. Write a Python program to create a tuple with different data types.
tupleWithMultipleDataTypes = ("hi", 1, False)

# 3. Write a Python program to create a tuple with numbers and print one item.
tupleWithNumbers = (1, 2, 3, 4, 5)
print(tupleWithNumbers[2])

# 4. Write a Python program to unpack a tuple in several variables.
tupleExample = (1, 4, 9)
variable1 = tupleExample[0]
variable2 = tupleExample[1]
variable3 = tupleExample[2]


# 5. Write a Python program to add an item in a tuple.
tupleAdd1 = (1, 2, 3)
tupleAdd2 = (4, 5, 6)
tupleAdd1 = tupleAdd1 + tupleAdd2

# 6. Write a Python program to convert a tuple to a string.
tupleToString = ("Hi ", "how ", "are ", "you", "?")
string = ''.join(tupleToString)
# print(string)

# 7. Write a Python program to get the 4th element and 4th element from the last of a tuple.
tupleElement = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(tupleElement[3])
fourthToLastElement = (len(tupleElement)) - 4
print(tupleElement[fourthToLastElement])

# 8. Write a Python program to create the colon of a tuple.

# 9. Write a Python program to find the repeated items of a tuple.

# 10. Write a Python program to check whether an element exists within a tuple.

# 11. Write a Python program to convert a list to a tuple.
# 12. Write a Python program to remove an item from a tuple.
# 13. Write a Python program to slice a tuple.
# 14. Write a Python program to find the index of an item of a tuple.
# 15. Write a Python program to find the length of a tuple.
# 16. Write a Python program to convert a tuple to a dictionary.
# 17. Write a Python program to unzip a list of tuples into individual lists.
# 18. Write a Python program to reverse a tuple.
# 19. Write a Python program to convert a list of tuples into a dictionary.
# 20. Write a Python program to print a tuple with string formatting.Sample tuple : (100, 200, 300)Output :This is a tuple (100, 200, 300)



# Sources:
# https://www.programiz.com/python-programming/tuple
# https://stackoverflow.com/questions/1380860/add-variables-to-tuple#:~:text=However%2C%20tuples%20in%20Python%20are,tuple%20once%20it%20is%20created.
# https://www.geeksforgeeks.org/python-program-to-convert-a-tuple-to-a-string/
