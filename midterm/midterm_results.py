# FILE NAME - midterm_results.py

# NAME: Nick Carlson
# DATE: 11/3/2025
# BRIEF DESCRIPTION: give a choice between calculating the area of either a circle or rectangle, then print the results


results = []


########## ENTER YER CODE BELOW THIS LINE ##########
import midterm_loop

print("Welcome to the Mathenator2000")

temp = midterm_loop.loop()
for i in temp:
    if i != None:
        results.append(i)

print("\n-------------------------\nA record of your results: ")
print(results)

print("\nThank you for using the Mathenator2000")
########### END YER CODE ABOVE THIS LINE ###########






########################################
#          SAMPLE OUTPUT
########################################

'''
Welcome to the Mathenator2000

Please choose from the following menu:
  1. Compute area of a circle
  2. Compute area of a rectangle

What is your choice? 1

What is the radius of the circle? 10
The area of the circle is 314.0

Would you like to play again (y/n)? y

Please choose from the following menu:
  1. Compute area of a circle
  2. Compute area of a rectangle

What is your choice? 2

What is the length of the rectangle? 10
What is the width of the rectangle? 20

Would you like to play again (y/n)? n

-------------------------
A record of your results: 
['The area of the circle is 314.0', 'The area of the rectangle is 200.0']

Thank you for using the Mathenator2000
'''


'''
Welcome to the Mathenator2000

Please choose from the following menu:
  1. Compute area of a circle
  2. Compute area of a rectangle

What is your choice? 2

What is the length of the rectangle? 0
What is the width of the rectangle? -1

Would you like to play again (y/n)? y

Please choose from the following menu:
  1. Compute area of a circle
  2. Compute area of a rectangle

What is your choice? 1

What is the radius of the circle? 1
The area of the circle is 3.14

Would you like to play again (y/n)? y

Please choose from the following menu:
  1. Compute area of a circle
  2. Compute area of a rectangle

What is your choice? 3

Invalid selection.

Would you like to play again (y/n)? n

-------------------------
A record of your results: 
['The area of the rectangle is -0.0', 'The area of the circle is 3.14']

Thank you for using the Mathenator2000
'''


'''
Welcome to the Mathenator2000

Please choose from the following menu:
  1. Compute area of a circle
  2. Compute area of a rectangle

What is your choice? 3

Invalid selection.

Would you like to play again (y/n)? n

-------------------------
A record of your results: 
[]

Thank you for using the Mathenator2000
'''