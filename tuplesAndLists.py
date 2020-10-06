# Aarian Dhanani
# 10/5/20
# Tuples and Lists Assignment

from copy import deepcopy

# 1. Write a Python program to create a tuple.
tuple1 = ("hi", "hello")

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
tuple1 = (1, 2, [], 4)
tuple2 = deepcopy(tuple1)
tuple2[2].append(3)
print(tuple2)

# 9. Write a Python program to find the repeated items of a tuple.
tupleRepeat = (1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10)
list1 = []
for x in range((len(tupleRepeat)) - 1):
    temporary = tupleRepeat.count(tupleRepeat[x])
    if temporary > 1 and list1.count(tupleRepeat[x]) == 0:
        print(tupleRepeat[x])
        list1.append(tupleRepeat[x])

# 10. Write a Python program to check whether an element exists within a tuple.
tupleElement2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
element = 3
if tupleElement2.count(element) > 0:
    print("Yes")
else:
    print("No")

# 11. Write a Python program to convert a list to a tuple.
listNew = ["hi", "ok", "hello"]
tupleNew = tuple(listNew)

# 12. Write a Python program to remove an item from a tuple.
# It is not possible to remove an item from a tuple.

# 13. Write a Python program to slice a tuple.
tupleSlice = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(tupleSlice[3:8])

# 14. Write a Python program to find the index of an item of a tuple.
tupleFind = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(tupleFind.index(5))


# 15. Write a Python program to find the length of a tuple.
tupleLength = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(len(tupleLength))

# 16. Write a Python program to convert a tuple to a dictionary.
# ?

# 17. Write a Python program to unzip a list of tuples into individual lists.
# ?

# 18. Write a Python program to reverse a tuple.
# 19. Write a Python program to convert a list of tuples into a dictionary.
# 20. Write a Python program to print a tuple with string formatting.Sample tuple : (100, 200, 300)Output :This is a tuple (100, 200, 300)
# 21. Write a Python program to replace last value of tuples in a list.Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
# 22. Write a Python program to remove an empty tuple(s) from a list of tuples.Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
# 23. Write a Python program to sort a tuple by its float element.Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]
# 24. Write a Python program to count the elements in a list until an element is a tuple.


# Sources:
# https://www.programiz.com/python-programming/tuple
# https://stackoverflow.com/questions/1380860/add-variables-to-tuple#:~:text=However%2C%20tuples%20in%20Python%20are,tuple%20once%20it%20is%20created.
# https://www.geeksforgeeks.org/python-program-to-convert-a-tuple-to-a-string/
# https://www.w3resource.com/python-exercises/tuple/python-tuple-exercise-8.php
# https://stackoverflow.com/questions/12836128/convert-list-to-tuple-in-python
# https://stackoverflow.com/questions/12836128/convert-list-to-tuple-in-python
# https://www.geeksforgeeks.org/python-convert-a-list-into-a-tuple/
# https://www.pythoncentral.io/how-to-slice-listsarrays-and-tuples-in-python/
# https://thispointer.com/python-how-to-find-an-element-in-tuple-by-value/
# https://stackoverflow.com/questions/31087111/typeerror-list-object-is-not-callable-in-python/55115952
