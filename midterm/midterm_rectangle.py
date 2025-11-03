# FILE NAME - midterm_rectangle.py

# NAME: Nick Carlson
# DATE: 11/3/2025
# BRIEF DESCRIPTION: Determine the area of a rectangle via two inputs

def rectangle():

    length = float(input("What is the length of the rectangle? "))
    width = float(input("What is the width of the rectangle? "))
    area = length * width
    print(f"The area of the rectangle is {area}\n")
    return "The area of the rectangle is " + str(area)