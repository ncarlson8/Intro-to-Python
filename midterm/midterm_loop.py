# FILE NAME - midterm_loop.py

# NAME: Nick Carlson
# DATE: 11/3/2025
# BRIEF DESCRIPTION: Add a loop function for when y is input

import midterm_choice

def loop():

    temp = []
    play = "y"
    while play == "y":
        temp.append(midterm_choice.choice())
        play = input("Would you like to play again (y/n)? ")
    return temp