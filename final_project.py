import random

"""
Aim of code to generate a list of names from a given 
list of names. The length of list should be asked for
and then returned
"""

"""
Control flow:
Ask user for input of the names
    Check for legit input (no numbers etc)
Ask user for length of list they wish to be returned
    Check input is positive intger, else re-ask until correct output
Randomly select x amount of names and output the list
"""

#Asks user for their shortlist of names
user_input_names = input('Please input your shortlist of names, make sure to separate the names by a single space. \n')

#Convert input to list and assign variable to length of list
user_list = user_input_names.split(' ')
user_length = len(user_list)

def length_input(user_length):

    """
    Ask user for length of list to return and checks input
    and if value accepted length will be returned 

    Args:
        THe length of the inputted list

    Returns:
        Outputs the length of the output lists
    """

    while True:
        try:
            #Asks user to input number from 1 to original list length - 1
            print('Input the length of list you would like returned')
            print(f"Min: 1 | Max: {user_length-1}")
            user_output_length = int(input())

            if (1 <= user_output_length <= user_length-1):
                print('Input accepted')
                return user_output_length
        
            else:
                #This code executes if int entered is not within bounds
                print("Input not accepted")
                print(f"Min: 1 | Max: {user_length-1}")
        
        except ValueError:
            #Executes if an integer is not entered
            print("Please enter a valid number")
        
#Variable set to length input from user
user_output_length = length_input(user_length)

def name_choser(user_output_length):

    """
    Removes number of items 

    Args:
        Amount of names required for final list

    Returns:
        Outputs list name 
    """

    while len(user_list) > (user_output_length):

        #Assign a random number between 0 and list size
        temp = random.randint(0, (len(user_list) - 1))

        #Remove the random index from list
        user_list.pop(temp)
    
    #For loop to print all the names in the list
    print('The names chosen are:')
    for x in range (len(user_list)):
        print(user_list[x])
    
name_choser(user_output_length)
