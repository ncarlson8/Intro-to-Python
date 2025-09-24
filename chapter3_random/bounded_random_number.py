# FILE NAME - bounded_random_number.py

# NAME: Nick Carlson
# DATE: 9/24/2025
# BRIEF DESCRIPTION: Generate a number between 1 and 10 with a user entered seed



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience

import random


########## ENTER YER CODE BELOW THIS LINE ##########

def main():
    bounded_random()

def bounded_random():
    ## TODO: Replace the code below with your code
    user_input = int(input("Enter an integer: "))
    random.seed(user_input)
    print(random.randint(1, 10))

main()


########### END YER CODE ABOVE THIS LINE ###########



########################################
#          SAMPLE OUTPUT
########################################

'''

Enter a seed for the random number generation: 33
10

'''



'''

Enter a seed for the random number generation: 32
2

'''



'''

Enter a seed for the random number generation: 100
3

'''



########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is a good way to remember if the arguments (parameters) for a bounded number are inclusive or exclusive?

an inclusive upper bound is not standard, randint is an excenption.




'''
