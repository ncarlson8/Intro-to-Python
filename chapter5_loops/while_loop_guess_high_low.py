# FILE NAME - while_loop_guess_high_low.py

# NAME: 
# DATE: 
# BRIEF DESCRIPTION:  



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience




SECRET_NUMBER = 33


########## ENTER YER CODE BELOW THIS LINE ##########
ui = 0
count = 0
while ui != SECRET_NUMBER:
    ui = int(input("Guess a number: "))
    count += 1
    if ui > SECRET_NUMBER:
        print("Your guess is too high.\n")
    elif ui < SECRET_NUMBER:
        print("Your guess is too low.\n")
print(f"\nYou guessed in {count} tries.")
########### END YER CODE ABOVE THIS LINE ###########




########################################
#          SAMPLE OUTPUT
########################################

'''
Guess a number: 22
Your guess is too low.

Guess a number: 44
Your guess is too high.

Guess a number: 33

You guessed in 3 tries.
'''


'''
Guess a number: 33

You guessed in 1 tries.
'''


'''
Guess a number: -9
Your guess is too low.

Guess a number: 100
Your guess is too high.

Guess a number: 30
Your guess is too low.

Guess a number: 32
Your guess is too low.

Guess a number: 34
Your guess is too high.

Guess a number: 33

You guessed in 6 tries.
'''

