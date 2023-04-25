import random

def pick_random_names_from_list(user_input):
    """
    Function takes names in a string and returns a specified number of random results

    Parameters
    -----
    user_input : string

    returns
    -----
    result : string
    """
    name_list = user_input.split(',')

    while True:
        shortlist_count = input('Enter the number of names you want selected: ')
        if shortlist_count.isdigit() and int(shortlist_count) > 0:
            shortlist_count = int(shortlist_count)
            if shortlist_count <= len(name_list):
                break
            else:
                print(f'You entered {shortlist_count}, but there are only {len(name_list)} names in the list. Please enter a smaller number.')
        else:
            print(f'You entered {shortlist_count}, but you must select a valid number of 1 or higher')

    random_names = random.sample(name_list, shortlist_count)
    print('Random names: ')
    for name in random_names:
        result = ', '.join(random_names)
        return result

def check_valid_input():
    """
    Function takes an input and validates that its not empty

    returns
    -----
    name_input : string
    """
    name_input = input('Enter a list of names separated by a comma: ')
    while len(name_input) == 0 or name_input.isspace():
        name_input = input('Enter a valid name or names please: ')
    return name_input

validated_input = check_valid_input()
random_names = pick_random_names_from_list(validated_input)
print(random_names)



