# Nick Carlson
# October 1, 2025
# Use the current hour to determine & print a greeting

from datetime import datetime
import pytz

# get the current date & time
victor_timezone = pytz.timezone('America/New_York') 
current_day_time = datetime.now(victor_timezone)
print(f"Current date & time: {current_day_time}")
    
# display the current time
print(f"Current time: {current_day_time.strftime('%H:%M:%S')}")

# extract the hour (0-23)
# 0 represents midnight, 1 represents 1 AM, ..., 23 represents 11 PM
# display the current hour
current_hour = current_day_time.hour
print(f"Current hour: {current_hour}")

### YOUR CODE BEGINS HERE!
if 5 <= current_hour <= 11:
    print("Good Morning!")
elif 12 <= current_hour <= 16:
    print("Good Afternoon!")
elif 17 <= current_hour <= 22:
    print("Good Evening!")
else:
    print("You should be sleeping!")
###


'''
datetime: https://docs.python.org/3/library/datetime.html
time zones - pytz: https://pypi.org/project/pytz/
'''