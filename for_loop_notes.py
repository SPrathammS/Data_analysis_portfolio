# print("This is for loops")
# drinks = ["sprite", "coke", "milkshake"]  #list in square brackets, items separated by commas and items held in inverted commas
# print (len(drinks))
# # # iteration- repitation of a process
# # print (drinks [1])  # typically to print each item in list individually, but can be done better with loops (repitation)
# for i in drinks:   # "i" is the iteration/ index variable and can be named anything. 
#     # i at each iteration, changes to next element in sequence 
#     print(i)
# for j in drinks:
#     print (" a great choice!")  # prints string for each index in the list

# web_users = [ "Praths", 
#              "Vish",
#              "Mak"]
# for user in web_users:
#     print(f"\nDear {user}!")
#     print("Thanks for using our website")
#     print("See you later - site team\n")
# # all lines get printed for each index
# "\n! is used as line breaker"

# # for loop runs for a FINITE amount of times- they will eventually stop
# # eg: ecomm webpage showing items in a row is basically a "for loop"- toys page eg.

# print (list(range(20)))
# for i in range(20):
#     print (i)
#    # range needs an argument- using start, stop and step
#    # for i in range (0,10,1) 

# total = sum(range(0,101))
# print (total)

total = 0

for i in range(1,101):
    total +=i
    
print(total)