# FILE NAME - midterm_choice.py

# NAME: Nick Carlson
# DATE: 11/3/2025
# BRIEF DESCRIPTION: Use a different function based on the answer given

import midterm_menu
import midterm_circle
import midterm_rectangle

def choice():
    midterm_menu.menu()

    choice = int(input("What is your choice? "))
    print()
    if choice == 1:
        return midterm_circle.circle()
    elif choice == 2:
        return midterm_rectangle.rectangle()
    else:
        print("Invalid selection.\n")