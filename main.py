import random

def random_names_generator():
    def input_name():
        """
        Function that takes names input and check if input is empty
        Returns
        ----
        user_names : str
        """
        
        not_valid_names = True
        while not_valid_names:
            user_names = input('Enter random names separared by space: \n')
            if not user_names:
                print('You have not entered any names. Please try again')        
            else:
                print(f'Thanks for entering {user_names}')
                not_valid_names = False

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

    def random_names(names, number):
        """
        Function that generates random number of names specified by the user
        Arguments
        ----
        names : str
        number : int    
        """

        name_list = names.split() 
        generated_random_names = random.sample(name_list, number)
        print(f'Random names generated are: {generated_random_names}')
    

    user_names = input_name()
    validated_number = input_number()
    random_names(user_names, validated_number)

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