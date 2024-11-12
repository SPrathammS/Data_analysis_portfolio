# print ("This is functions notes file")
# def goodbye():
#     print("Goodbye!")

# goodbye()

# def cash_withdrawal (amount, accnum):
#     print (f"You have withdrawn £{amount} from your account: {accnum}")
    
# cash_withdrawal(250, 78596412)
# cash_withdrawal(500, 12566325)

# def take_order(size, type):
#     print (f" You have ordered a {size} {type}.")
# size = input("Enter your drink size:")
# type = input("Enter your drink type:")
# take_order(size, type)

# # Activity 1

# #n= input ("Enter name: ")

# def wish (name):
#  print(f"Happy Birthday to you,\nHappy Birthday to you,\nHappy Birthday dear {name},\nHappy Birthday to youuuuu!")
 
# #wish (n)
# wish (input ("Enter birthday name: "))

# Activity 2

order_count = 0
topping1= input ("Enter first topping: ")
topping2= input("Enter second topping: ")
crust= input("Enter crust type: ")
size=input ("Enter size: ")

def take_order (topping1, topping2, crust, size ):
    global order_count
    print(f"You ordered {size} {crust} pizza with {topping1} and {topping2}")
    order_count +=1
    print(f"Your order number is {order_count}")
    

take_order (topping1, topping2, crust, size )    
take_order (topping1, topping2, crust, size )    
take_order (topping1, topping2, crust, size )    

# # Activity 3

# dataset = [34,67,5,81,2,45,9,23,55,41,42,84,109, 109, 109]

# def mean (dataset):
#    print(f" The mean is: {sum(dataset)/len(dataset)} ")

# mean (dataset)
