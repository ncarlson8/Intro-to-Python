# FILE NAME - convert_C_to_F_02.py

# NAME: Nick Carlson
# DATE: 9/29/2025
# BRIEF DESCRIPTION: Convert between celsius and fahrenheit and vice versa



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########
print("===== Temperature converter =====\n\n 1. Convert from Celsius to Fahrenheit \n 2. Convert from Fahrenheit to Celsius")
choice = input("\nPlease choose from the above menu: ")
temp = float(input("Enter a temperature to convert: "))
if choice == "1":
    conv_temp = temp * 1.8 + 32
    print(f"\n{temp} degrees Celsius is {conv_temp} degrees Fahrenheit.")
elif choice == "2":
    conv_temp = (temp - 32) / 1.8
    print(f"\n{temp} degrees Fahrenheit is {conv_temp} degrees Celsius.")
########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: 32

32.0 degrees Fahrenheit is 0.0 degrees Celsius.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: -40

-40.0 degrees Fahrenheit is -40.0 degrees Celsius.
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is one lesson you learned in this lab?

Detail is important.





'''