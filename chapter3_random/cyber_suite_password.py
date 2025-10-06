# FILE NAME - cyber_suite_password.py

# NAME: Nick Carlson
# DATE: 9/24/2025
# BRIEF DESCRIPTION: Generate a random password



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience

import random


########## ENTER YER CODE BELOW THIS LINE ##########
import string

def main():
    generate_password()

def generate_password():
    ## TODO: Replace the code below with your code
    user_input = int(input("\nEnter a seed for the random number generation: "))
    random.seed(user_input)
    spec1 = random.choice(['!','@','#','$','&','(',')',',','-','_'])
    lowercase1 = random.choice(string.ascii_lowercase)
    uppercase1 = random.choice(string.ascii_uppercase)
    lowercase2 = random.choice(string.ascii_lowercase)
    uppercase2 = random.choice(string.ascii_uppercase)
    num1 = random.choice(string.digits)
    num2 = random.choice(string.digits)
    spec2 = random.choice(['!','@','#','$','&','(',')',',','-','_'])
    print(f"Your random password is: \n{spec1}{lowercase1}{uppercase1}{lowercase2}{uppercase2}{num1}{num2}{spec2}\n")

main()


########### END YER CODE ABOVE THIS LINE ###########



########################################
#          SAMPLE OUTPUT
########################################

'''

Enter a seed for the random number generation: 33
Your random password is:
_fUhI78-

'''



'''

Enter a seed for the random number generation: 22
Your random password is:
#hAtO21(

'''



'''

Enter a seed for the random number generation: 0
Your random password is:
)yNbI87)

'''



########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What was the hardest part of completing this lab?

Making sure the arrays are correct.




2. What value do you see in the `string` module?

It allows certain commonly used strings to be easier to implement.




'''
