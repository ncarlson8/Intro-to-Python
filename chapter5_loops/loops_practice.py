import time

#ny_cities = ["New York", "Buffalo", "Yonkers", "Rochester", "Syracuse"]

#for city in ny_cities:
#    print(f"{city} is one of the five biggest cities in the state of New York.")
#    if city == "New York":
#        print("New York is the largest city in the US.")

#n = 1

#while n < 11:
#    print(n, end = " ")
#    n = n + 1

#n = 500
#while n >= 0:
#    print(n)
#    n = n - 100

#phrase = "mmm"
#while phrase != "stop":
#    phrase = input("Do you wish to continue? ")

for num in range(10, 0, -1):
    print(num)
    time.sleep(1)
print("Go!")

num = 10
while num >= 1:
    print(num)
    num-=1
    time.sleep(1)
print("Go!")
