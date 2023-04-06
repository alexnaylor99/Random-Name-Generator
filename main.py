import random
import re

def user_inputs():
    """Ask user for inputs."""
    name_list = ''
    num_of_names = 0
    while True:
        name_list = input("Enter names separated by a comma: ")
        name_list = remove_whitespace_after_commas(name_list)
        if not check_punctuation(name_list):
            print("Error: Name list should only contain letters and commas.")
            continue
        name_list = remove_duplicates(name_list.split(','))
        num_of_names = get_valid_num_of_names(name_list)
        break
    return name_list, num_of_names

def get_valid_num_of_names(name_list):
    """Confirms user input for the number is an integer and lower than the number of names in the list submitted"""
    while True:
        num_of_names = input(f"Enter a number lower than {len(name_list)} to randomly select that number of names from the list: ")
        if not num_of_names.isdigit():
            print("Error: Number must be an integer.")
        elif int(num_of_names) > len(name_list):
            print(f"Error: Number must be {len(name_list)} or lower.")
        else:
            return int(num_of_names)

def check_punctuation(name_list):
    """Check if name list contains only letters and commas."""
    if re.search(r"[^a-zA-Z,\s]", name_list):
        return False
    return True

def remove_duplicates(name_list):
    """Remove duplicates from the name list."""
    return list(set(name_list))

def remove_whitespace_after_commas(name_list):
    """Remove whitespace after commas in the name list."""
    return re.sub(r',\s*', ',', name_list)

def generate_random_names():
    """Generates then prints randomly selected names from the list of names submitted by the user"""
    name_list, num_of_names = user_inputs()
    selected_names = set()
    while len(selected_names) < num_of_names:
        selected_names.add(random.choice(name_list))
    print("Randomly selected names:")
    for i, name in enumerate(selected_names, 1):
        print(f"{i}: {name}")


generate_random_names()
