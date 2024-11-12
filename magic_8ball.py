
# # # Create an 8ball program
 
# # # Create two lists - one of "good" results and one of "bad" results.
# # # allow for input.
# # # after the question is asked, gen a random number; odd = bad, even = good.
# # # use a random method to pick a random fortune from the appropriate list and print it out.
 
# # # Use Colorama to display bad fortunes in red text and good fortunes in green text.
 
# # import random
 
# # good_response = ["It is certain",
# #                  "It is decidedly so",
# #                  "Without a doubt",
# #                  "Yes definitely",
# #                  "You may rely on it"]
 
# # bad_response = ["Don't count on it",
# #                 "My reply is no",
# #                 "My sources say no",
# #                 "Outlook not so good",
# #                 "Very doubtful",
# #                 ]
 
# # even_num = 2
# # rdm_num = (random.randint(1,2))

# # rdm_good = random.choice(good_response)
# # rdm_bad = random.choice(bad_response)
 
# # while rdm_num != even_num:
# #     print(f" {rdm_bad}") 

# import random
# user_question = input("Enter your question here: ")

# random_number = random.randint(1,2)

# good_response = ["It is certain",
#                  "It is decidedly so",
#                  "Without a doubt",
#                  "Yes definitely",
#                  "You may rely on it"]
 
# bad_response = ["Don't count on it",
#                 "My reply is no",
#                 "My sources say no",
#                 "Outlook not so good",
#                 "Very doubtful",
#                 ]

# if random_number % 2 != 0:   
#     selection = random.choice(bad_response)
#     print(f"{selection}")
# else:
#     selection = random.choice(good_response)
#     print(f"{selection}")
# ------------------------------------------------------------------------------------------------------------------------------

import random
from colorama import Fore, Style, Back #* we have imported 'colorama' and 'random' library and used their functions

def function():    #* we are defining a function that will ask a question, that generates a random number and chooses an item from the relevant list according to set condition.
 input("What is your question?: ")   #user input 

 rdm_num = (random.randint(1,2))   # generation of random number between integers (1,2)- 50% chances of odd/even
 print(rdm_num)
#* here are two lists, one good and bad, from which the program will randomly select depending on the number generated
 good_response = ["It is certain", # A list of common good responses for a magic 8ball
                 "It is decidedly so",
                 "Without a doubt",
                 "Yes definitely",
                 "You may rely on it"]

 bad_response = ["Don't count on it", # A list of common bad responses for a magic 8ball
                "My reply is no",
                "My sources say no",
                "Outlook not so good",
                "Very doubtful",
                ]

 even_num = 2
# Ron suggested even_num = 2 and the randint be (1,3) allowing us to easily determine an odd or even number, 
# After discussion it was suggested that 'randint' being (1,2) would allow for a fairer game, while accomplishing the same task.
#* random.choice was a function we researched to allow us pull a random entry from the lists we have
 random_good = random.choice(good_response) # random.choice pulls a random entry from the list and stored in a variable which would be used ahead for colorama function/styling.
 random_bad = random.choice(bad_response) 
#* if-else condition and output with colorama effects.
 if rdm_num != even_num: #* This checks that the random number is not equal to "2" which is our even number, We decided to use an if statement rather than a while loop.
    print(Fore.RED+f"{random_bad}") # if it is not an even number it prints a [bad response]
 else:
    print (Fore.GREEN+f"{random_good}") # if it is an even number it prints a [good response]

 print(Style.RESET_ALL) # allows the terminal to reset the colour
#* we give the user a choice if they want to ask another question 
# variable used for specific user input and modified to match condition ahead
 repeat= input("Do you want to ask another question? (Y/N): ").strip().lower()
 while repeat != "y" and repeat != "n":  # recursion/ 'while loop' used to run until user input matches to given conditions 
   print("Invalid entry. Please type Y/N")
   repeat= input("Do you want to ask another question? (Y/N): ").strip().lower()
 if repeat == "y":  # revisit the initial function and repeat the whole process
  function ()
 elif repeat == "n":  # exit the program. Will use ascii
  print(r"""       Thank You 
         .-'-.
       /   _   \
       |  (8)  |
       \   ^   /
        '-...-'
      For Playing""")   # used ascii to show 8 ball.
# it gives this error message "unterminated string literal" as it cant ignore escape characters such as \.
# to avoid this, we used the "raw strings" prefix "r", "r" will help maintain proper formatting, while using triple quotes (""") handles multi-line strings.

 
function() # calling function() to start the program