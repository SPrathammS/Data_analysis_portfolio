# Activity 1
name= input("Enter your name: ").capitalize() #.capitalize() to ensure first letter is in capital
age= int(input("Enter your age: "))
colour= input("Enter your favourite colour: ").lower()
print (f"{name} is {age} years old and their favourite colour is {colour}.")

# Activity 2
num1= int(input("Enter the first number: "))
num2= int(input("Enter the second number: "))
add=(num1+num2)
sub= (num1-num2)
div= (num1/num2)
mult= (num1*num2)
exp= (num1**num2)
mod= (num1%num2)
print (f"The addition of {num1} and {num2} is: {add}")
# ALTERNATIVE 
# print (f"{num1}+{num2}={num1+num2}") or print (f"{num1}+{num2}={add}")
print (f"The subtraction of {num2} from {num1} is: {sub} ")
print (f"The division of {num1} by {num2} is: {div} ")
print (f"The base of {num1} to the power of {num2} is: {exp} ")
print (f"The modulus of {num1} and {num2} is: {mod} ")

# Activity 3
app= int(input(" Enter the number of apples you want: "))
ban= int(input(" Enter the number of bananas you want: "))
app_cost= (app*.25)  # avoid floating points (.25)- AVOID
print (f"The cost of {app} apples: £{app_cost}")
ban_cost= (ban*.50)
print (f"The cost of {ban} bananas: £{ban_cost}")       
total_cost= (app*.25)+(ban*.50)
print (f"The total cost of {app} apples and {ban} bananas amounts to: £{total_cost} ")

# Activity 3 stretch
print (f"The cost of {app} apples rounded is: £{total_cost:.2f}")  
# format the number upto 2 decimal place (:.2f)

# ----------better way activity 3------------

apple_cost = 25
apple_amount = int(input("How many apples would you like to buy?"))

apple_total = apple_cost * apple_amount

banana_cost = 50
banana_amount = int(input("How many bananas would you like to buy?"))

banana_total = banana_cost * banana_amount

total = apple_total + banana_total

print(f"You bought {apple_amount} apples")

print(f"You bought {banana_amount} bananas")

print(f"Your total is {total}p")
print(f"Your total is £{total/100:.2f}")
 