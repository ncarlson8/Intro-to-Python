import datetime

print("Welcome to Hotel California, where you can check in, but can never leave. You can actually leave though.")

name = input("What is your name? ")
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print("Welcome, " + name)

vip_file = open("vip.txt", "r")
vip_list = vip_file.readlines()
print(vip_list)
vip_status = False
for guest_name in vip_list:
    if guest_name.strip() == name:
        vip_status = True
        print("VIP")

file = open("all_guests.txt", "a")
file.write(f"{name}, VIP: {vip_status}, Arrival Time: {timestamp}\n")
file.close()