def input_name():
    """
    Function that takes names input
    Returns
    ----
    user_names : str
    """
    
    user_names = input('Enter random names separared by space: \n')
    print(f'Thanks for entering {user_names}')
    print(type(user_names))
    return user_names

    
def input_number():
    """
    Function that takes number input
    Returns
    ----
    number : str
    """
    number = input('Enter a number to randomly select names of your list: \n')
    print(type(number))
    return number


input_name()
input_number()