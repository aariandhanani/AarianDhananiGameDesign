#Aarian Dhanani
#9/15/20
#NOT DONE YET

number = 30;

if number > 30:
    print("Number must be less than or equal to 50")
    exit()

for x in range(1, (number + 1)):
    print(x, end = " ")

print("\n")

for x in range(1, (number + 1)):
    print(x)

print("\n")

for x in range(1, (number + 1)):
    for y in range(x):
        if x <= 9:
            print(x, end = " ")
        else:
            print(x, end = "")
    print("")

# for x in range(1, (number + 1)):
#     for z in range(number - x):
#         if x <= 9:
#             print(x, end = " ")
#         else:
#             print(x, end = "")
#         print(" ", end = "")
#     for y in range(x):
#         print(x, end = "")
#     print("")
#
# for x in range(1, (number + 1)):
#     for z in range(number - x):
#         print(" ", end = "")
#     for y in range(x):
#         print(x, end = "")
#     print(" ", end = "")
#     for y in range(x):
#         print(x, end = "")
#     print("")
