#Aarian Dhanani
#array printing

myList = [2, 4, 5, 7, 8, 9]
yourList = [98, 87, 65]
myFruit = ["Apple", "Banana", "Orange"]

# myFruit.remove("Apple")

myFruit.pop(0)

del myFruit[0]
myFruit.append("Mango")
myFruit.insert(1, "Kiwi")

print(myFruit)

print(len(myFruit))
# print(myList[1])
# print(myList[-2])
print(myList[1:4])

if 4 in myList:
    print("yes")

if "berries" in myFruit:
    print("I love banana")
else:
    print("buy some berries")

ourList = myList + yourList
print(ourList)

myList.extend(myFruit)

print(myList)


myFruit.sort()
print(myFruit)

# for x in myList:
#     print(x)
