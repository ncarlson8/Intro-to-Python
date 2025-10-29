# FILE NAME - calc.py

# NAME: Nick CArlson
# DATE: 10/29/2025
# BRIEF DESCRIPTION: A simple four function calculator



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience


########## ENTER YER CODE BELOW THIS LINE ##########
import calc_util

print("\nWelcome to the Calculator\n")

num1 = float(input("What is the first number? "))
num2 = float(input("What is the second number? "))
print()

calc_util.add(num1, num2)
calc_util.subtract(num1, num2)
calc_util.multiply(num1, num2)
calc_util.divide(num1, num2)

print("\nHave a nice, mathy day.")
########### END YER CODE ABOVE THIS LINE ###########




########################################
#          SAMPLE OUTPUT
########################################

'''

Welcome to the Calculator

What is the first number? 10
What is the second number? 5

SUM =  15.0
DIFFERENCE =  5.0
PRODUCT =  50.0
QUOTIENT =  2.0

Have a nice, mathy day.
'''


'''
Welcome to the Calculator

What is the first number? 0
What is the second number? 1

SUM =  1.0
DIFFERENCE =  -1.0
PRODUCT =  0.0
QUOTIENT =  0.0

Have a nice, mathy day.

'''


########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What was the hardest part of completing this lab? 

remembering to use floats instead of ints




2. How did you decide if the functions in the `calc_util` module should return or print?

the resulting values aren't used for anything besides a print statement, so I used a print



'''
