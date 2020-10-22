# Aarian Dhanani
# October 22nd, 2020
# Treasure hunt game

import random

rows, cols = (5, 5)

arr = [[0 for i in range(cols)] for j in range(rows)]

word = random.choice(gameWords)

# arr =  [[0]*cols]*rows

# arr[0][0] = 1

for row in arr:
    print(row)

# Sources:
# https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/
