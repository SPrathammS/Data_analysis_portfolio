# 
# FOREGROUND- color of text itself
# background- 
# style- 

# DOCUMENTATION from library important- can use hep of gpt to make it more readable and accessible

# from colorama import Fore, Back, Style

print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')

from datetime import datetime

def days_lived(birth_date_str):
    # Convert the input birth date string to a datetime object
    birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")
    
    # Get today's date
    today = datetime.now()
    
    # Calculate the difference in days
    days = (today - birth_date).days
    
    return days

# Input birth date in the format YYYY-MM-DD
birth_date_str = input("Enter your birth date (YYYY-MM-DD): ")
days = days_lived(birth_date_str)
print(f"You have lived {days} days.")
