items = ["shirts", "shorts", "socks", "hat"]

# print all items in the list
for item in items:
    print(item)

# print a specific item in the list
print(items[0])
print(items[-1])
# check to see if an item is in the list
if "shirts" in items:
    print("Good job")
else:
    print("Go get a shirt")
# add an item to the list
items.append("toiletries")

# remove an item from the list
items.remove("hat")

for item in items:
    print(item)

# list length
print(len(items))

# sorting
items.sort()

# reverse
items.reverse()

for item in items:
    print(item)

# print the list
print(items)
print("\nX ", end="")
print(*items, sep="\nX ")

# insert
items.insert(0, "snacks")
print(items[0])