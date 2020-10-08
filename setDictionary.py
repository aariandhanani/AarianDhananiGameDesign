thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)

print("banana" in thisset)

if "kiwi" in thisset:
    thisset.add("orange")
elif "cherry" in thisset:
    thisset.update(["mango", "berries", "kiwi"])

print(thisset)
