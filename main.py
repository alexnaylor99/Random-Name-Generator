import random

def input_name():
    """
    Asks the user to input a list of names, validates them, removes duplicates and returns a list of valid names.

    Returns:
        name_list (list): A list of names to be selected from.
    """
    # Ask the user to input a string of names separated by spaces
    name_input = input("Please enter alpha names separated by spaces: ")
    # Split and remove duplicates
    name_list = list(set(name_input.split()))  
    # Check if the names are alphabet and transform the names to be capitalized format
    name_list = [name.title() for name in name_list if name.isalpha()] 

    # Check if at least one valid name was entered, if not, the user will be asked to input again
    if not name_list:
        print("Please enter at least one valid name.")
        return input_name()
    else:
    # Show the user how many names are added to the database and the added names
        print(f"The following {len(name_list)} names were added to the database: {', '.join(name_list)}")
        return name_list

def input_length(name_list):
    """
    Ask the user to input a number of names they want to be randomly selected from a database.

    Parameters:
        name_list (list): A list of names to be selected from.

    Returns:
        name_num (int): The number of names to be selected.
    """
    while True:
        try:
            # Ask the user to input a number of names to select randomly
            name_num = int(input(f"How many names do you want randomly selected from the database? Min: 1, Max: {len(name_list)}\nanswer: "))
            # Make sure the input number is between 1 and the the number of names inputed, if not, the user will be asked to input again
            if 1 <= name_num <= len(name_list):
                return name_num
            else:
                print(f"Please enter a number between 1 and {len(name_list)}")
        # If the user enters a value that cannot be converted to an integer, the user will be asked to input again
        except ValueError:
            print("Please enter a valid number.")

def print_names(name_list, name_num):
    # Select a random sample of names from the name_list and print them
    random_names = random.sample(name_list, name_num)
    print("Random names:", *random_names, sep='\n- ')

if __name__ == "__main__":
    # Get a list of unique names from the user
    name_list = input_name()
    # Get the number of names to select randomly from the user
    name_num = input_length(name_list)
    # Print the randomly selected names
    print_names(name_list, name_num)
