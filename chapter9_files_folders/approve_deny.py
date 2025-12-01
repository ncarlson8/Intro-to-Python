# FILE NAME - approve_deny.py

# NAME: Nick Carlson
# DATE: 11/19/2025
# BRIEF DESCRIPTION: Ask for a URL, compare it to what is on an approve file and a deny file, print the status of the URL, then if it isn't on oeither file, then add it to a review file.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience






########## ENTER YER CODE BELOW THIS LINE ##########
url = input("Enter a URL to access: ")
file = open("approve.txt", "r")

approve_list = file.readlines()
approved = False
for url in approve_list:
    if url.strip() == url:
        approved = True
        print("\nACCESS GRANTED")
        print(f"--------------------------------------------------\n       CONTENT FROM: {url}")
        print("--------------------------------------------------\nThis website has been verified as safe by your organization.\nFeel free to browse this content for business or educational purposes.\nRemember to follow the organization's acceptable use policy.")
        print("--------------------------------------------------")

file.close()
file = open("deny.txt", "r")

deny_list = file.readlines()
denied = False
for url in deny_list:
    if url.strip() == url:
        deny = True
        print("\nACCESS DENIED")
        print(f"--------------------------------------------------\n       BLOCKED URL: {url}")
        print("--------------------------------------------------\nThis website has been blocked by your organization's web filter.\nReason: This URL is on the deny list.\nIf you believe this is an error, please contact IT support.")
        print("--------------------------------------------------")

file.close()

if approved == False and denied == False:
    print("\nURL UNDER REVIEW")
    print(f"--------------------------------------------------\n       PENDING REVIEW: {url}")
    print("--------------------------------------------------\nThis website is not on the approve or deny lists.\nIt has been submitted for review by the security team.\nAccess is currently restricted until review is complete.\nPlease check back later or contact IT if urgent access is needed.")
    print("--------------------------------------------------")
    print("\nURL has been added to review.txt for security team review.")
    file = open("review.txt", "a")
    file.write(f"{url}\n")
    file.close()

print("\nThis access attempt has been logged to log.txt")
file = open("log.txt", "a")
file.write(url)
########### END YER CODE ABOVE THIS LINE ###########




########################################
#          SAMPLE OUTPUT
########################################

'''
Enter a URL to access: www.flcc.edu

ACCESS GRANTED
--------------------------------------------------
       CONTENT FROM: www.flcc.edu
--------------------------------------------------
This website has been verified as safe by your organization.
Feel free to browse this content for business or educational purposes.
Remember to follow the organization's acceptable use policy.
--------------------------------------------------

This access attempt has been logged to log.txt
'''

'''
Enter a URL to access: www.phishingdemo.org

ACCESS DENIED
--------------------------------------------------
       BLOCKED URL: www.phishingdemo.org
--------------------------------------------------
This website has been blocked by your organization's web filter.
Reason: This URL is on the deny list.
If you believe this is an error, please contact IT support.
--------------------------------------------------

This access attempt has been logged to log.txt
'''

'''
Enter a URL to access: www.opencompsci.com

URL UNDER REVIEW
--------------------------------------------------
       PENDING REVIEW: www.opencompsci.com
--------------------------------------------------
This website is not on the approve or deny lists.
It has been submitted for review by the security team.
Access is currently restricted until review is complete.
Please check back later or contact IT if urgent access is needed.
--------------------------------------------------

URL has been added to review.txt for security team review.

This access attempt has been logged to log.txt
'''

