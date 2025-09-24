# FILE NAME - dice.py

# NAME: Nick Carlson
# DATE: 9/24/2025
# BRIEF DESCRIPTION: Takes a seed and generates two random integers from 1 and 6



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience

import random


########## ENTER YER CODE BELOW THIS LINE ##########


def main():
    roll_die()

def roll_die():
    ## TODO: Replace the code below with your code
    user_input = int(input("Enter a seed for the random number generation: "))
    random.seed(user_input)
    print(f"Die roll one is {random.randint(1, 6)}\nDie roll two is {random.randint(1, 6)}")


main()


########### END YER CODE ABOVE THIS LINE ###########



########################################
#          SAMPLE OUTPUT
########################################

'''

Enter a seed for the random number generation: 33
Die roll one is 5
Die roll two is 2

'''



'''

Enter a seed for the random number generation: 22
Die roll one is 2
Die roll two is 2

'''



'''

Enter a seed for the random number generation: -30
Die roll one is 5
Die roll two is 3

'''



########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is the purpose of "seeding" the random number generator?

Seedin the random number generator allows for consistency, and that is useful when debugging or grading.




'''
