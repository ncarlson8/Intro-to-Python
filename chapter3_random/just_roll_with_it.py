import random

roll1 = random.randint(1, 30)
#print(roll1)

roll2 = random.randint(0, 9)
roll3 = random.randint(0, 9)
roll_output = 10 * roll2 + roll3

if roll_output == 0:
    roll_output = 100

#print(f"roll2 is {roll2}")
#print(f"roll3 is {roll3}")
#print(f"roll_output is {roll_output}")


wheel = random.randint(1, 46)
#print(wheel)

chance = 30 * 100 * 46

if roll1 == 22 and roll_output == 22 and wheel == 2:
    print("$1 Million dollar WINNER!!!!")
else:
    print("Sorry, no big money for you")
    if roll1 == 22:
        print("you won some lettuce though.")
    if roll_output == 22:
        print("you won a teddy bear though")
    if wheel == 22:
        print("You won a foam die though")