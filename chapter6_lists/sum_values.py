# FILE NAME - sum_values.py

# NAME: Nick Carlson
# DATE: 10/22/2025
# BRIEF DESCRIPTION: Sum each day's failed logins.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience







#########################################
#               YOUR JOB:               #
#                                       #
# 1. Sum all the items in the list. You #
#    might find the `sum()` function    #
#    handy.                             #
#                                       #
#########################################

########## ENTER YER CODE BELOW THIS LINE ##########
attempts = []
print("Please enter failed login attempts")
print("==================================\n")
attempts.append(int(input("  Monday:    ")))
attempts.append(int(input("  Tuesday:   ")))
attempts.append(int(input("  Wednesday: ")))
attempts.append(int(input("  Thursday:  ")))
attempts.append(int(input("  Friday:    ")))
print("\n\n===== FAILED LOGIN ATTEMPTS ANALYZER =====\n")
print(f"Total failed login attempts for the week: {sum(attempts)}\n")

if sum(attempts) > 100:
    print("SECURITY ALERT: Weekly threshold of 100 attempts has been exceeded!")
    print("Recommendation: Investigate for potential brute force attacks.")
else:
    print("Everything seems normal. It's quiet. Too quiet.")
    print("Recommendation: Continue routine monitoring.")
########### END YER CODE ABOVE THIS LINE ###########
    




########################################
#          SAMPLE OUTPUT
########################################

'''
Please enter failed login attempts
==================================

  Monday:    1
  Tuesday:   2
  Wednesday: 3
  Thursday:  4
  Friday:    5


===== FAILED LOGIN ATTEMPTS ANALYZER =====

Total failed login attempts for the week: 15

Everything seems normal. It's quiet. Too quiet.
Recommendation: Continue routine monitoring.
'''


'''
Please enter failed login attempts
==================================

  Monday:    12
  Tuesday:   10
  Wednesday: 4
  Thursday:  0
  Friday:    88


===== FAILED LOGIN ATTEMPTS ANALYZER =====

Total failed login attempts for the week: 114

SECURITY ALERT: Weekly threshold of 100 attempts has been exceeded!
Recommendation: Investigate for potential brute force attacks.
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. How did you sum the element in the list?

with the sum() function





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