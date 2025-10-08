# FILE NAME - rectangle_redux.py

# NAME: Nick Carlson
# DATE: 10/8/2025
# BRIEF DESCRIPTION: create a rectangle with a certain height based on user input



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience






########## ENTER YER CODE BELOW THIS LINE ##########
height = int(input("How tall would you like the rectangle? "))
print("*****")

for n in range(1, height + 1):
    print("*   *")

print("*****")
########### END YER CODE ABOVE THIS LINE ###########




########################################
#          SAMPLE OUTPUT
########################################

'''
How tall would you like the rectangle? 3
*****
*   *
*   *
*   *
*****
'''


'''
How tall would you like the rectangle? 1
*****
*   *
*****
'''


'''
How tall would you like the rectangle? 0
*****
*****
'''


'''
How tall would you like the rectangle? 10
*****
*   *
*   *
*   *
*   *
*   *
*   *
*   *
*   *
*   *
*   *
*****
'''

