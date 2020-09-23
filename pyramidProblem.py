#Aarian Dhanani
#Pyramid Challenge

# for x in range(1, 9):
#     print("1", end = "")
#     if x != 1:
#         for z in range(2, x + 1):
#             print(z, end = "")
#     print("")


for x in range(1, 9):
    for y in range(8 - x):
        print(" ", end = "")
    if x != 1:
        for z in range(2, x + 1):
            print(9 - z, end = "")

    print("1", end = "")
    if x != 1:
        for z in range(2, x + 1):
            print(z, end = "")
    print("")
