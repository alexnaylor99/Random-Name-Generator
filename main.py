import random

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
        number = input()   
        if number.isnumeric() and number != "0":
            number = int(number)
            not_valid_number = False
        else:
            print('Please, enter a number greater than 0')

    return number

def random_names():
    name_list = user_names.split() 
    generated_random_names = random.sample(name_list, validated_number)
    print(generated_random_names)
   

user_names = input_name()
validated_number = input_number()
random_names()