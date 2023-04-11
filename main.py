import random
import re

def random_names_generator():
    def input_name():
        """
        Function that takes names input and check if input is valid
        Returns
        ----
        name_list : list
        """
        
        not_valid_names = True
        while not_valid_names:
            user_names = input('Enter random names separared by space: \n')
            if not user_names:
                print('You have not entered any names. Please try again')        
            elif not re.search(r'^[a-zA-Z ]+$', user_names):
                print('Names should only contain letters and be separated by spaces')
            else:
                print(f'Thanks for entering: {user_names}')
                name_list = user_names.split() 
                not_valid_names = False

        return name_list
        
    def input_number(name_list):
        """
        Function that takes and validate number input from user
        Arguments
        ----
        name_list : list
        Returns
        ----
        number : int
        """

        print(f'Enter a number that is equal or lower than {len(name_list)} to randomly select names from your list: ')
        not_valid_number = True
        while not_valid_number:
            number = input()
            if not number.isnumeric():
                print('Please enter a valid number:')
            elif number == "0":
                print('Please, enter a number greater than 0:')
            elif int(number) > len(name_list):
                print(f'Please, enter a number that is equal or lower than {len(name_list)}:')
            else:
                return int(number)
       

    def random_names():
        """
        Function that generates random number of names specified by the user 
        """
        
        name_list = input_name()
        number_of_names = input_number(name_list)
        if len(name_list) == 1:
            print('You only entered 1 name!')
        else:
            generated_random_names = random.sample(name_list, number_of_names)
            print(f'Random names generated are: {generated_random_names}')

    random_names()

random_names_generator()

another_try = True
while another_try:
    print('Do you want to try again? (Y/N): ')
    new_names = input().upper()
    if new_names == 'Y':
        random_names_generator()
    else: 
        print('Thanks for using this app!')
        another_try = False