import random

# congrat the parents
print("congratulations parents!")

#Create a function to validate user input and generate a list

def validate_input(input_str):

    input_list = input_str.split(",")
    if len(input_list) == 1 and input_list[0] == '':
        return False
    for item in input_list:
        if not item.strip().isalpha():
            return False
        return True

#Implement a function to randomly select an item from a given list based on user input

def generate_name(first_name, last_name):
    first_name = random.choice(first_name)
    last_name = random.choice(last_name)
    return f"{first_name.capitalize()} {last_name.capitalize()}"


#Implement input validation for first name
while True:
    first_name_str = input(
        "Enter you comma separenedt list for your first name: ")
    if validate_input(first_name_str):
        first_name = [name.strip() for name in first_name_str.split(",")]
        break
    print("Invalid input. please enter a comma-separated list for your first name.")

#Implement last name input validation
while True:
    last_name_str = input(
        "Enter you comma separented list for your last name: ")
    if validate_input(last_name_str):
        last_name = [name.strip() for name in last_name_str.split(",")]
        break
    print("Invalid input. please endter a comma-separated list for your last name.")

#Implement input validation for number of generated instances
while True:
    num_name_str = input("How many names do you want to gernerate?  ")
    if num_name_str.isdigit() and int(num_name_str) >= 1:
        num_name = int(num_name_str)
        break
    print("Invalid input. please enter a postive number or number, like (1,2,3). ")

#Add output for generated names
for i in range(num_name):
    name = generate_name(first_name, last_name)
    print(name)
