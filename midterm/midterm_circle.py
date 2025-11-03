# FILE NAME - midterm_circle.py

# NAME: Nick Carlson
# DATE: 11/3/2025
# BRIEF DESCRIPTION: A function for determining the area of a circle

def circle():
    rad = float(input("What is the radius of the circle? "))
    area = 3.14 * (rad ** 2)
    print(f"The area of the circle is {area}\n")
    return "The area of the circle is " + str(area)