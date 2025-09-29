# Nick Carlson
# 9/29/2025
# User selects a language fromfrom a menu
# then greets the user in that language

print("Hello! Which language would you like to learn?")
print("Choose:\n\t(1)French \n\t(2)Spanish \n\t(3)German \n\t(4)Swedish")

choice = int(input("Select a number: "))

if choice == 1:
    print("HELLO in French is BONJOUR")
    print("Bonjour!")
elif choice == 2:
    print("HELLO in Spanish is HOLA")
    print("Hola!")
elif choice == 3:
    print("HELLO in German is HALLO")
    print("Hallo!")
elif choice == 4:
    print("HELLO in Swedish is HEJ")
    print("Hej!")
else:
    print("That is not a valid choice.")

