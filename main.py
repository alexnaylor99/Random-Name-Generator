import random
import re

def get_user_inputs():
    """Ask user for inputs."""
    name_list = ''
    num_of_names = 0
    while True:
        # Ask the user to input a list of names separated by commas
        name_list = input("Enter names separated by a comma: ")
        #  Check the list of names is not empty
        if not check_name_list_not_empty(name_list):
            print("Error: You did not submit any names. Please enter a list of names separated by a comma: ")
            continue
        # Remove whitespace after each comma in the input
        name_list = remove_whitespace_after_commas(name_list)
        # Check that the input contains only letters, hyphens, and commas
        if not check_punctuation(name_list):
            print("Error: Name list should only contain letters, hyphens, and commas.")
            continue
        # Remove duplicates from the input list of names
        name_list = remove_duplicates(name_list.split(','))
        # Check for and remove any empty strings in the input list
        name_list = check_for_empty_string(name_list)
        # Get a valid number of names to randomly select from the list
        num_of_names = get_valid_num_of_names(name_list)
        break
    return name_list, num_of_names

def get_valid_num_of_names(name_list):
    """Get a user input for the number that is an integer and lower than the number of names in the list submitted."""
    while True:
        # Ask the user to input a number lower than the number of names in the list
        num_of_names = input(f"Enter a number {len(name_list)} or lower to randomly select that number of names from the list: ")
        # Check that the input is a valid integer
        if not num_of_names.isdigit():
            print("Error: Number must be an integer.")
        # Check that the input number is less than or equal to the number of names in the list
        elif int(num_of_names) > len(name_list):
            print(f"Error: Number must be {len(name_list)} or lower.")
        # Check that the input number is greater than 0
        elif int(num_of_names) <= 0:
            print(f"Error: Number must be greater than 0")
        else:
            return int(num_of_names)

def check_punctuation(name_list):
    """Check if name list contains only letters, hyphens, and commas."""
    # Check if the input contains any characters other than letters, hyphens, commas, or whitespace
    if re.search(r"[^a-zA-Z,\-\s]", name_list):
        return False
    return True

def remove_duplicates(name_list):
    """Remove duplicates from the name list."""
    # Convert the input list to a set to remove duplicates, then convert back to a list
    return list(set(name_list))

def remove_whitespace_after_commas(name_list):
    """Remove whitespace after commas in the name list."""
    # Replace any whitespace that comes after a comma with just a comma
    return re.sub(r',\s*', ',', name_list)

def check_name_list_not_empty(name_list):
    """Check if the name list is not empty."""
    # Check if the input list is empty
    if not name_list:
        return False
    return True

def check_for_empty_string(name_list):
    """Check for empty strings in a list and remove them."""
    # Use a list comprehension to remove any empty strings from the input list
    name_list = [name for name in name_list if name != '']
    return name_list

def select_random_names():
    """Generate then print randomly selected names from the list of names submitted by the user"""
    # Get the input list of names and the number of names to select
    name_list, num_of_names = get_user_inputs()
    selected_names = set()
    while len(selected_names) < num_of_names:
        selected_names.add(random.choice(name_list))
    print("Randomly selected names:")
    for i, name in enumerate(selected_names, 1):
        print(f"{i}: {name}")


select_random_names()
