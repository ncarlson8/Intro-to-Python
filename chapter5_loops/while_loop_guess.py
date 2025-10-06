# FILE NAME - while_loop_guess.py

# NAME: Nick Carlson
# DATE: 10/6/2025
# BRIEF DESCRIPTION: Continue a while loop until the user inputs 33



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience






########## ENTER YER CODE BELOW THIS LINE ##########
ui = 0
count = 0
while ui != 33:
    ui = int(input("Guess a number: "))
    count += 1
print(f"You guessed in {count} tries.")
########### END YER CODE ABOVE THIS LINE ###########




########################################
#          SAMPLE OUTPUT
########################################

'''
Guess a number: 22
Guess a number: 44
Guess a number: 33
You guessed in 3 tries.
'''


'''
Guess a number: 33
You guessed in 1 tries.
'''


'''
Guess a number: -9
Guess a number: 100
Guess a number: 30
Guess a number: 32
Guess a number: 34
Guess a number: 33
You guessed in 6 tries.
'''

