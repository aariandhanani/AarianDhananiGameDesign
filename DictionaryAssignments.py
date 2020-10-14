# Aarian Dhanani
import operator
import random

# Write a Python script to sort (ascending and descending) a dictionary by value.
dictionary1 =  {0: 1, 4: 5, 2: 3}

sortedDictionaryAscending1 = sorted(dictionary1.items(), key=operator.itemgetter(1))
print(sortedDictionaryAscending1)

sortedDictionaryDescending1 = sorted(dictionary1.items(), key=operator.itemgetter(1), reverse=True)
print(sortedDictionaryDescending1)

# Write a Python script to add a key to a dictionary.
#        Sample Dictionary : {0: 10, 1: 20}
#        Expected Result : {0: 10, 1: 20, 2: 30}

dictionary2 =  {0: 1, 2: 3, 4: 5}
dictionary2[6] = 7
print(dictionary2)


# Write a Python script to concatenate the following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

question3dictionary1 = {1:10, 2:20}
question3dictionary2 = {3:30, 4:40}
question3dictionary3 = {5:50, 6:60}

question3dictionary = {**question3dictionary1, **question3dictionary2, **question3dictionary3}
print(question3dictionary)

# Write a Python script to check whether a given key already exists in a dictionary.

dictionary4 =  {0: 1, 4: 5, 2: 3}

key = 0

if key in dictionary4:
    print("Yes")
else:
    print("No")

# Write a Python program to iterate over dictionaries using for loops.

dictionary5 =  {0: 1, 2: 3, 4: 5}
for variable, value in dictionary5.items():
    print(value)

# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

n = 5
dictionary6 =  {}
for value1 in range(1, n + 1):
    dictionary6[value1] = (value1 * value1)
print(dictionary6)

# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.  Sample Dictionary: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

dictionary7 =  {}
for value1 in range(1, 16):
    dictionary7[value1] = (value1 * value1)
print(dictionary7)

# Write a Python script to merge two Python dictionaries.

question8dictionary1 = {1:10, 2:20}
question8dictionary2 = {3:30, 4:40}

question8dictionary = {**question8dictionary1, **question8dictionary2}

print(question8dictionary)

# Write a Python program to iterate over dictionaries using for loops.

dictionary9 =  {0: 1, 2: 3, 4: 5}
for variable, value in dictionary9.items():
    print(value)

# Write a Python program to sum all the items in a dictionary.

dictionary10 =  {0: 1, 2: 3, 4: 5}
print(sum(dictionary10.values()))


# Sources:
# https://www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.php
# https://stackoverflow.com/questions/1024847/how-can-i-add-new-keys-to-a-dictionary
# https://dev.to/0xbf/merge-multiple-dictionaries-python-tips-26ag
# https://stackoverflow.com/questions/1602934/check-if-a-given-key-already-exists-in-a-dictionary
# https://stackoverflow.com/questions/3294889/iterating-over-dictionaries-using-for-loops
# https://stackoverflow.com/questions/4880960/how-to-sum-all-the-values-in-a-dictionary
