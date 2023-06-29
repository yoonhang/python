import pyautogui
import time

print(pyautogui.position())
pyautogui.click(100,100)
pyautogui.typewrite('Hello aaaaaeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')



import datetime

# Prompt the user to enter their birth year, month, and day
birth_year = int(input("Enter your birth year (YYYY): "))
birth_month = int(input("Enter your birth month (MM): "))
birth_day = int(input("Enter your birth day (DD): "))

# Get the current date
now = datetime.datetime.now()

# Calculate the user's age
age = now.year - birth_year + 1

# Adjust the age based on the birth month and day
if now.month < birth_month:
    age -= 1
elif now.month == birth_month and now.day < birth_day:
    age -= 1

# Print the user's age in Korean age
print("Your Korean age is:", age)
