for x in range(1, 10):
    for y in range(x):
        print("*", end = "")
    for z in range(9 - x):
        print(" ", end = "")


    for y in range(10 - x):
        print("*", end = "")
    for z in range(x - 1):
        print(" ", end = "")


    for z in range(x - 1):
        print(" ", end = "")
    for y in range(10 - x):
        print("*", end = "")


    for z in range(9 - x):
        print(" ", end = "")
    for y in range(x):
        print("*", end = "")
    print(" ", end = "")
    print("")
