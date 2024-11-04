# print ("This is my variables file")

# Activity1:Print 8th character from string in Uppercase
# print ("All Around The World"[7].upper())

# intro to variable
# my_name= "Prathamm"
# # print (my_name)
# # my_name="Surana"  (if same variable updated, code reads from top to bottom for output!)
# # print (my_name)

# # variable in sentence (format string or f string)
# age= "21"
# fav_drink= "mocha"
# print (f"{my_name} is {age} and his favourite drink is {fav_drink}!")

# # user input
# user_name= input("Type your name here: ")
# print (f"Hello {user_name}, good to see you today!")
# print (type(user_name))

# # maths
# print(3+2)
# print(3-2)
# print(3*2)
# print(3**2)
# print(6/2)  #divide
# print(6%2)  #modulus or remainder
# print(16%3)

# # amount withdrawal ATM 
# balance= 100
# amt_to_withdraw= 20
# balance= balance-amt_to_withdraw
# print (balance)
# # balance -= amt_to_withdraw

# casting for input as integer using 'int()' constructor.

# print("Type two numbers to multiply them")
# num1= int(input("num1: "))
# num2= int(input("num2: "))

# print (num1*num2)

# Activity 2: user has 100 as balance and ask for amt to withdraw
balance=100
amt_to_withdraw= int(input("Enter amount to withdraw: "))
balance -= amt_to_withdraw
print(f"You have withdrawn {amt_to_withdraw} and your remaining balance is: {balance}")