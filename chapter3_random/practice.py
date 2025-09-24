import random

seed_from_user = int(input("Type a seed(int): "))
random.seed(seed_from_user)

#print(random.random())

print(random.randint(1,20))