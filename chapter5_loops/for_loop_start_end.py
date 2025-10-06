# FILE NAME - for_loop_start_end.py

# NAME: Nick Carlson
# DATE: 10/6/2025
# BRIEF DESCRIPTION: Output every integer between a starting and ending point



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience






########## ENTER YER CODE BELOW THIS LINE ##########
start = int(input("Starting point: "))
end = int(input("Ending point: "))

for n in range(start, end + 1):
    print(n , end = " ")
########### END YER CODE ABOVE THIS LINE ###########




########################################
#          SAMPLE OUTPUT
########################################

'''
Starting point: 3
Ending point: 7
3 4 5 6 7
'''


'''
Starting point: -4
Ending point: 4
-4 -3 -2 -1 0 1 2 3 4
'''


'''
Starting point: 0
Ending point: 1
0 1
'''
