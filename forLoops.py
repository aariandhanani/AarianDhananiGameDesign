#Aarian Dhanani
#9/15/20


for x in range(1, 10):
    print(x, end = " ")

print("\n")

for x in range(1, 10):
    print(x)

print("\n")

for x in range(1, 10):
    for y in range(x):
        print(x, end = "")
    print("")

for x in range(1, 10):
    for z in range(9 - x):
        print(" ", end = "")
    for y in range(x):
        print(x, end = "")
    print("")

for x in range(1, 10):
    for z in range(9 - x):
        print(" ", end = "")
    for y in range(x):
        print(x, end = "")
    print(" ", end = "")
    for y in range(x):
        print(x, end = "")
    print("")
