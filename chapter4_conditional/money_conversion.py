# Nick Carlson
# 9/29/2025
# Convert from one currency to another

print("Where are you going to?")
print("I for India, U for the United Kingdom, C for China, and M for Mexico.")
dest = input(print("Type your destination: "))
amt = float(input(print("How many USD would you like to convert?")))

# USD to Rupees 1 to 88.7
if dest == 'I':
    conv_amt = amt * 88.7
    currency = "Indian Rupees"

# USD to GBP 1 to .75
elif dest == 'U':
    conv_amt = amt * .75
    currency = "Great British Pounds"

# USD to Yuan 1 to 7.12
elif dest == 'C':
    conv_amt = amt * 7.12
    currency = "Chinese Yuan"

# USD to Pesos 1 to 18.33
elif dest == 'M':
    conv_amt = amt * 18.33
    currency = "Mexican Pesos"

else:
    currency = "NOT SELECTED"

print(f"Your ${amt} converts to {conv_amt:.2f} {currency}.")
