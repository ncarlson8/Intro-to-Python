# FILE NAME - authenticate.py

# NAME: Nick Carlson
# DATE: 10/6/2025
# BRIEF DESCRIPTION: Enter a password until it is correct



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience






########## ENTER YER CODE BELOW THIS LINE ##########
password = "tooManySecrets"
given = input("Enter password: ")
while given != password:
    print("\nPassword does not match.")
    given = input("Enter password: ")
print("\nAccess granted.")
########### END YER CODE ABOVE THIS LINE ###########




########################################
#          SAMPLE OUTPUT
########################################

'''
Enter password: a

Password does not match.
Enter password: b

Password does not match.
Enter password: tooManySecrets

Access granted.
'''


'''
Enter password: tooManySecrets

Access granted.
'''


'''
Enter password: toomanysecrets

Password does not match.
Enter password: TOOMANYSECRETS

Password does not match.
Enter password: too_Many_Secrets

Password does not match.
Enter password: tooManySecrets

Access granted.
'''

