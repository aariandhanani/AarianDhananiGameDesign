thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)

print("banana" in thisset)

if "kiwi" in thisset:
    thisset.add("orange")
elif "cherry" in thisset:
    thisset.update(["mango", "berries", "kiwi"])

print(len(thisset))

print(thisset)

otherSet = {1, 2, 3, 4}
anotherSet = {"kiwi", "mango", "papaya", "watermelon"}

print(thisset.intersection(anotherSet))
print(thisset.union(anotherSet))

myDictionary =  {"Name": "Aarian", "Age": 16, "School": "Greenhill School"}
print("The name of the students is", myDictionary["Name"])
print("This person is", myDictionary["Age"], "years old.")
print(myDictionary.keys())
