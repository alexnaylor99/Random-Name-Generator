import random

def main():

    """
    Main wrapper function for the random name generator
    
    Function will prompt user for 2 input:
        1) a list of names
        2) a number of names to select

    Function will print out the randomly selected sample.
    """

    print('-----------------------------')
    print('Roman\'s Random Name Generator')
    print('----------------------------- \n')
    
    #Name inputs
    while True:
        try:
            names_str = str(input('Please input a list of names separated by commas: '))
            
            #use helper function to validate string
            list_of_valid_names = nameCheck(names_str)
        except ValueError:
            #invalid name list --> prompt user to correct input
            print(
                '\nInvalid list of names!\nCheck the following:\
                \n\t1) Names are valid (contain only letter characters)\
                \n\t2) Names separated by commas\
                \n\nPlease try again...\n'
                )
            continue
        else:
            #valid name list --> break out of while loop
            break

    num_of_names = len(list_of_valid_names)
    print() #adding white space


    #Number inputs
    while True:
        try:
            sample_size = int(input('How many names would you like to select from your list? '))
        except: 
            #invalid sample number --> prompt user to correct input
            print('\nPlease enter a valid number of names\n')
            continue
        else:
            if (0 < sample_size <= num_of_names):
                #valid sample number --> break out of while loop
                break
            else:
                #invalid sample number --> prompt user to correct input
                print(
                    '\nInvalid number of names!\nCheck the following:\
                        \n\t 1) Your number is positive\
                        \n\t 2) Your number does not exceed the total size of the list\
                        \n\nPlease try again...'
                    )
                continue

    #use random module to create sample list of names
    selected_names = random.sample(list_of_valid_names, sample_size)
    print() #adding white space

    # print selected names to user
    print("Randomly selected names:")
    output_str = ', '.join(selected_names)
    print(output_str.strip(','))
    print() #adding white space



def nameCheck(name_string):
    """
    Function checks whether user name list is valid.
    If valid the function outputs a list of capitalized names
    If invalid the function raises a ValueError exception

    Parameters
    -----
    name_string: str

    Returns
    -----
    name_list: list (of strings)
    """

    #list comprehension to convert input string into list of names
    name_list = [name.strip() for name in name_string.split(',')] 
    for name in name_list:
        if not name.isalpha():
            #error is triggered if name has any non-alphabetic characters
            raise ValueError
    
    #capitalize each name with list comprehension
    name_list = [name.capitalize() for name in name_list]
    
    return name_list
        


if __name__ == "__main__":
   main()