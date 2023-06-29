import datetime

def calculate_age(birthdate):
    # Convert the birthdate string to a datetime object
    birthdate_obj = datetime.datetime.strptime(birthdate, '%Y-%m-%d')

    # Get the current date
    now = datetime.datetime.now()

    # Calculate the user's age
    age = now.year - birthdate_obj.year

    # Adjust the age based on the birth month and day
    if now.month < birthdate_obj.month:
        age -= 1
    elif now.month == birthdate_obj.month and now.day < birthdate_obj.day:
        age -= 1

    return age

age = calculate_age('1973-07-01')
print("Your age is:", age)
