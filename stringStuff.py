#Aarian Dhanani
#September 30th, 2020

strVar = "My name is Aarian"

print(strVar)
print(len(strVar))
print(strVar[len(strVar) - 1])

indexNumber = strVar.find("name")
print(indexNumber)
print(strVar[indexNumber:indexNumber + 4])
print(strVar[indexNumber:])
print(strVar[ :indexNumber])
print(strVar.replace("name", "first name"))
strVar = strVar.replace("name", "first name")
print(strVar)
print(strVar.upper())
print(strVar.lower())
print(strVar)

print(strVar.reverse())


# var = ["M", "y", " ", "n", "a", "m", "e", " ", "i", "s", " ", "A", "a", "r", "i", "a", "n"]
#
# for x in range(len(var)):
#     print(var[x], end = "")
