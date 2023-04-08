def input_name():
    """
    Function that takes names input
    Returns
    ----
    user_names : str
    """
    
    user_names = input('Enter random names separared by space: \n')        
    print(f'Thanks for entering {user_names}')

    return user_names

    
def input_number():
    """
    Function that takes and validate number input from user
    Returns
    ----
    number : int
    """
    print('Enter a number to randomly select names of your list: ')
    not_valid_number = True
    while not_valid_number:
        number = int(input())   
        if number > 0:
            not_valid_number = False
        else:
            print('Please, enter a number greater than 0')
    return number


input_name()
input_number()