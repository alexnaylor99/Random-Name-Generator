# A function that takes a list of names and a number as arguments.
# The function should return x number of names randomly.

import random

def random_name_generator(list_names, num_names):
    '''
    Takes in a list of names and an amount of names desired, 
    then uses the random module to return a list of names.
    
    Parameters
    ----------
    list_names : List of strings
    num_names : Integer

    Returns
    -------
    Function returns a list of names
    '''
    shortlist = random.sample(list_names, num_names)
    return shortlist


# Ask the user to input a list of names separated by a space and create a list.
if __name__ == '__main__':
    names = input('Enter a list of names that you are '
                  'choosing from separated by a space: ')
    list_names = names.split()

    # Ask the user to input an integer and validate. 
    # If it is not an integer, as the user to try again. 
    while True:
        try:
            num_names = int(input(f'You have {len(list_names)} names in your list. '
                                  'How many names do you want: '))
            if num_names <= 0:
                print('You must choose a number greater than 0. Try again')
                continue
            break
        except Exception as e:
            print(f'Error: {e}\nTry again')
    
    # Generate the shortlist. If number of desired names is equal or less
    # than the length of the list of names, return that list.
    if len(list_names) > num_names:
        shortlist = random_name_generator(list_names, num_names)
    else:
        shortlist = list_names

    # If there are not enough names in the list, let the user know.
    if len(list_names) < num_names:
        print('There aren\'t enough names on the list! Printing anyways.')

    # Print the shortlist.
    if shortlist:
        print('Here is your shortlist:')
        for count, name in enumerate(shortlist, 1):
            print(f'{count}. {name}')