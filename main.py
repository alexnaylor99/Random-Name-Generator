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



if __name__ == '__main__':
    
    # Prompt the user to input a list of names and split them into a list.
    while True:
        names = input('Enter a list of names that you are '
                  'choosing from, separated by a space (eg: "Anna Elsa Moana"): ')
        
        # Check if the user has input names.
        if names == '':
            print('You must enter at lease 1 name. Try again.')
            continue
        
        list_names = names.split()
        break


    while True:
        # Prompt the user to input an integer and validate.
        try:
            num_names = int(input(f'You have {len(list_names)} names in your list. '
                                  'How many names do you want?\n'))
            if num_names <= 0:
                print('You must choose a number greater than 0. Try again')
                continue
            break
        except ValueError as e:
            print(f'Error: {e}.\nYou must enter an integer. Try again')
    
    # Generate the shortlist. 
    if len(list_names) > num_names:
        shortlist = random_name_generator(list_names, num_names)

    # Return the whole list if the number of names is less than the number required.
    else:
        shortlist = list_names

    # If there are not enough names in the list, let the user know.
    if len(list_names) < num_names:
        print(f'There are less than {num_names} names in the list. '
              'All names in the list have been included in the shortlist.')

    # Print the shortlist.
    if shortlist:
        print('Here is your shortlist:')
        for count, name in enumerate(shortlist, 1):
            print(f'{count}. {name}')
