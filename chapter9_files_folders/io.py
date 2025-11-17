print("Hello")
# name = input("What is your name? ")
# print(f"Welcome, {name}")

# file = open("visitors.txt", "a") #append
# file.write(name + "\n")
# file.close()

file = open("visitors.txt", "r")
# print(file)
# print(file.name)
print(file.read())
print(file.readlines())
file.close()