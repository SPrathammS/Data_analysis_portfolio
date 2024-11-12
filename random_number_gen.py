# library
import random

# print(random.random())
# print(random.uniform(1,10))
# print (random.randint(1,10))

user_number = int(input("enter your number: "))
comp_number = random.randint(1,50)

while user_number != comp_number:
    print (f"PC picked {comp_number}, whereas you picked {user_number}. They don't match.")
    comp_number = random.randint(1,50)

print (f"PC picked {comp_number}, whereas you picked {user_number}. Congratulations, they match. ")
