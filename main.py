import random

def input_name():
    """
    Asks the user to input a list of names, validates them, removes duplicates and returns a list of valid names.
    """
    # Ask the user to input a string of names separated by spaces
    name_input = input("Please enter alpha names separated by spaces: ")
    name_list = list(set(name_input.split()))  # Split and remove duplicates
    name_list = [name.title() for name in name_list if name.isalpha()]  # Validate names

    # Check if at least one valid name was entered
    if not name_list:
        print("Please enter at least one valid name.")
        return input_name()
    else:
        print(f"The following {len(name_list)} names were added to the database: {', '.join(name_list)}")
        return name_list

def input_length(name_list):
    """
    Asks the user for the number of names to select randomly from the list.
    """
    # Ask the user to input a number of names to select randomly
    while True:
        try:
            name_num = int(input(f"How many names do you want randomly selected from the database? Min: 1, Max: {len(name_list)}\nanswer: "))
            if 1 <= name_num <= len(name_list):
                return name_num
            else:
                print(f"Please enter a number between 1 and {len(name_list)}")
        except ValueError:
            print("Please enter a valid number.")

def print_names(name_list, name_num):
    # Select a random sample of names from the name_list and print them
    random_names = random.sample(name_list, name_num)
    print("Random names: ")
    for n in random_names:
        print (n)
    print("Thanks for using the app! ")

if __name__ == "__main__":
    # Get a list of unique names from the user
    name_list = input_name()
    # Get the number of names to select randomly from the user
    name_num = input_length(name_list)
    # Print the randomly selected names
    print_names(name_list, name_num)
