# FILE NAME - password_strength_test.py

# NAME: Nick Carlson
# DATE: 10/8/2025
# BRIEF DESCRIPTION: Determine the strength of a password based on a few criteria



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience






########## ENTER YER CODE BELOW THIS LINE ##########
import string
spec = ['!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}','|',';',':','\'','\\','"',',','.','<','>','/','?']

print(f"===== PASSWORD STRENGTH CHECKER =====\nThis tool analyzes your password and rates its strength.\n")
password = input("Enter a password to check: ")

points = 0
up_count = 0
low_count = 0
spec_count = 0
digit_count = 0
type_count = 0
length = len(password)

print(f"\n===== PASSWORD ANALYSIS =====")

if length >= 12:
    points += 25
elif length >= 8:
    points += 15
elif length >= 6:
    points += 10

for char in password:
    if char in string.ascii_uppercase:
        up_count += 1
    elif char in string.ascii_lowercase:
        low_count += 1
    elif char in spec:
        spec_count += 1
    elif char in string.digits:
        digit_count += 1

if up_count > 0:
    type_count += 1
    points += 15
if low_count > 0:
    type_count += 1
    points += 15
if spec_count > 0:
    type_count += 1
    points += 15
if digit_count > 0:
    type_count += 1
    points += 15

if type_count >= 3:
    points += 15

strength = ""
if points >= 80:
    strength = "STRONG"
elif points >= 60:
    strength = "MODERATE"
elif points >= 40:
    strength = "WEAK"
else:
    strength = "VERY WEAK"

print(f"Length: {length} characters")
print(f"Uppercase letters: {up_count}")
print(f"Lowercase letters: {low_count}")
print(f"Digits: {digit_count}")
print(f"Special characters: {spec_count}")

print(f"\nSecurity Score: {points}/100")
print(f"Strength Assessment: {strength}")

print("\n===== IMPROVEMENT SUGGESTIONS =====")

if points >= 100:
    print("- Excellent password! Remember to use different passwords for different accounts.")
else:
    if length < 12:
        print("- Use at least 12 characters for better security")
    if up_count == 0:
        print("- Add uppercase letters (A-Z)")
    if low_count == 0:
        print("- Add lowercase letters (a-z)")
    if digit_count == 0:
        print("- Add numbers (0-9)")
    if spec_count == 0:
        print("- Add special characters (!@#$%^&*)")
########### END YER CODE ABOVE THIS LINE ###########




########################################
#          SAMPLE OUTPUT
########################################

'''
===== PASSWORD STRENGTH CHECKER =====
This tool analyzes your password and rates its strength.

Enter a password to check: password

===== PASSWORD ANALYSIS =====
Length: 8 characters
Uppercase letters: 0
Lowercase letters: 8
Digits: 0
Special characters: 0

Security Score: 30/100
Strength Assessment: VERY WEAK

===== IMPROVEMENT SUGGESTIONS =====
- Use at least 12 characters for better security
- Add uppercase letters (A-Z)
- Add numbers (0-9)
- Add special characters (!@#$%^&*)
'''


'''
This tool analyzes your password and rates its strength.

Enter a password to check: p@SSword!

===== PASSWORD ANALYSIS =====
Length: 9 characters
Uppercase letters: 2
Lowercase letters: 5
Digits: 0
Special characters: 2

Security Score: 75/100
Strength Assessment: MODERATE

===== IMPROVEMENT SUGGESTIONS =====
- Use at least 12 characters for better security
- Add numbers (0-9)
'''


'''
===== PASSWORD STRENGTH CHECKER =====
This tool analyzes your password and rates its strength.

Enter a password to check: 4$DL_dsa_dsf!#

===== PASSWORD ANALYSIS =====
Length: 14 characters
Uppercase letters: 2
Lowercase letters: 6
Digits: 1
Special characters: 5

Security Score: 100/100
Strength Assessment: STRONG

===== IMPROVEMENT SUGGESTIONS =====
- Excellent password! Remember to use different passwords for different accounts.
'''
