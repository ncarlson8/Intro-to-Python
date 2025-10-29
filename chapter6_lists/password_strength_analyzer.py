# FILE NAME - password_strength_analyzer.py

# NAME: Nick Carlson
# DATE: 10/22/2025
# BRIEF DESCRIPTION: checks a password's strength



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience


import random


########## ENTER YER CODE BELOW THIS LINE ##########
import string

password = input("Enter your password: ")
print(f"\nPassword Analysis Report\n-------------------------")

points = 0
up_count = 0
low_count = 0
spec_count = 0
digit_count = 0
length = len(password)

if length >= 15:
    points += 8
    print(f"LENGTH: 8 points ({length} characters)")
elif length >= 8:
    points += 5
    print(f"LENGTH: 5 points ({length} characters)")
else:
    print(f"LENGTH: 0 points ({length} characters)")

for char in password:
    if char in string.ascii_uppercase:
        up_count += 1
    elif char in string.ascii_lowercase:
        low_count += 1
    elif char in string.digits:
        digit_count += 1
    else:
        spec_count += 1
    

if up_count > 2:
    points += 8
    print(f"UPPERCASE: 8 points ({up_count} uppercase letter(s))")
elif up_count == 2:
    points += 4
    print(f"UPPERCASE: 4 points ({up_count} uppercase letter(s))")
elif up_count == 1:
    points += 2
    print(f"UPPERCASE: 2 points ({up_count} uppercase letter(s))")
else:
    print(f"UPPERCASE: 0 points ({up_count} uppercase letter(s))")
if low_count > 2:
    points += 8
    print(f"LOWERCASE: 8 points ({low_count} lowercase letter(s))")
elif low_count == 2:
    points += 4
    print(f"LOWERCASE: 4 points ({low_count} lowercase letter(s))")
elif low_count == 1:
    points += 2
    print(f"LOWERCASE: 2 points ({low_count} lowercase letter(s))")
else:
    print(f"LOWERCASE: 0 points ({low_count} lowercase letter(s))")
if digit_count > 2:
    points += 8
    print(f"NUMBERS: 8 points ({digit_count} number(s))")
elif digit_count == 2:
    points += 4
    print(f"NUMBERS: 4 points ({digit_count} number(s))")
elif digit_count == 1:
    points += 2
    print(f"NUMBERS: 2 points ({digit_count} number(s))")
else:
    print(f"NUMBERS: 0 points ({digit_count} number(s))")
if spec_count > 2:
    points += 8
    print(f"SPECIAL CHARACTERS: 8 points ({spec_count} special character(s))")
elif spec_count == 2:
    points += 4
    print(f"SPECIAL CHARACTERS: 4 points ({spec_count} special character(s))")
elif spec_count == 1:
    points += 2
    print(f"SPECIAL CHARACTERS: 2 points ({spec_count} special character(s))")
else:
    print(f"SPECIAL CHARACTERS: 0 points ({spec_count} special character(s))")
    

print(f"\nTotal Score: {points/40}")
print(f"Strength Percentage: {points*2.5}%")
########### END YER CODE ABOVE THIS LINE ###########










########################################
#          SAMPLE OUTPUT
########################################

'''
Enter your password: password

Password Analysis Report
-------------------------
LENGTH: 5 points (8 characters)
UPPERCASE: 0 points (0 uppercase letter(s))
LOWERCASE: 8 points (8 lowercase letter(s))
NUMBERS: 0 points (0 number(s))
SPECIAL CHARACTERS: 0 points (0 special character(s))

Total Score: 0.325
Strength Percentage: 32.5%
'''

'''
Enter your password: p@$$WORD

Password Analysis Report
-------------------------
LENGTH: 5 points (8 characters)
UPPERCASE: 8 points (4 uppercase letter(s))
LOWERCASE: 2 points (1 lowercase letter(s))
NUMBERS: 0 points (0 number(s))
SPECIAL CHARACTERS: 8 points (3 special character(s))

Total Score: 0.575
Strength Percentage: 57.49999999999999%
'''

'''
Enter your password: 123PASwor

Password Analysis Report
-------------------------
LENGTH: 5 points (9 characters)
UPPERCASE: 8 points (3 uppercase letter(s))
LOWERCASE: 8 points (3 lowercase letter(s))
NUMBERS: 8 points (3 number(s))
SPECIAL CHARACTERS: 0 points (0 special character(s))

Total Score: 0.725
Strength Percentage: 72.5%
'''

'''
Enter your password: 123pasWOR!@#

Password Analysis Report
-------------------------
LENGTH: 5 points (12 characters)
UPPERCASE: 8 points (3 uppercase letter(s))
LOWERCASE: 8 points (3 lowercase letter(s))
NUMBERS: 8 points (3 number(s))
SPECIAL CHARACTERS: 8 points (3 special character(s))

Total Score: 0.925
Strength Percentage: 92.5%
'''

'''
Enter your password: 123pasWOR!@#888888888888

Password Analysis Report
-------------------------
LENGTH: 8 points (24 characters)
UPPERCASE: 8 points (3 uppercase letter(s))
LOWERCASE: 8 points (3 lowercase letter(s))
NUMBERS: 8 points (15 number(s))
SPECIAL CHARACTERS: 8 points (3 special character(s))

Total Score: 1.0
Strength Percentage: 100.0%
'''


########################################
#          REFLECTION QUESTIONS
########################################

'''

1. This is one of your first experiences with larger programs - what are three things
   that were challenging for you?

I just modified my existing code to better fit this program, this just required a bit more detail.





'''



########################################
#            ATTESTATION
########################################

'''
It is critical in this class that you understand the concepts as we explore them because
those concepts are required understanding for entry level programming. Reliance on resources
like AI and internet sites like Chegg, CourseHero, StackOverflow, and general Google results
may impede your understanding. Please rate how well you understand the concepts in this lab: 

[ ] I understand very little about this lab.
[ ] I am about 50/50 on this lab; I get parts of it but not the whole picture.
[ ] I pretty much get it.
[X] I'm solid. Totally got it.

'''