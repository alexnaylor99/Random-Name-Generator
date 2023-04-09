'''This Python script allows users to input a list of names and then randomly select a specified number of names from that list. 
The program will prompt the user to enter names until they are ready to select a random name.'''

import random
import sys
from subprocess import call

num_input = 0
name_input = None
names = []

#Re-run the app to play again
def restartApp():
    '''This function will restart the app if the user requests at the end of the previous game'''
    call(["python", "main-option-2.py"])

#Choose an amount of random outputs
def addNum():
    '''This function converts the string input into an int and uses it to select a random number of names from the list'''
    num_input = input(f"Enter a number between 1 and {len(names)}: ")

    validateNum(num_input)
        
    converted = float(num_input[0])

    newN = int(converted)

    while newN > len(names) or newN <= 0:

        num_input = input(f"Number entered must be between 1 and {len(names)} inclusive: ")
        
        newN = int(num_input)

    indices = []

    for i in range(newN):

        def newNum():

            rNum = random.randint(1, len(names))

            while rNum in indices:

                rNum = random.randint(1, len(names))

            else:

                return rNum
            
        indices.append(newNum())

    output = []

    for j in indices:

        output.append(names[j-1])

    print(output)

    again = input('Would you like to play again? Enter Y for yes or anything else to exit: ')

    if again == 'Y' or again == 'y':
        restartApp()
    else:
        sys.exit()  
     
    #return output

#Add names to the list
def enterName():
    '''This function allows user to keep adding names to the list after they've been validated'''
    name_input = input("Enter a name and press enter to add it to the list otherwise just press enter to stop: ")

    if name_input != '':

        validateName(name_input)

    else:

        validateEntKey(name_input)

#Validate reason for pressing enter
def validateEntKey(name_input):
    '''This function will validate whether enter key was pressed to add another name or stop adding names'''
    if name_input == '' and len(names) <= 1:

        print('The list must have two or more names to continue')

        name_input = None

        enterName()

    elif name_input == '' and len(names) > 1:

        name_input = None

        print('Continue')

        addNum()

#Validate users input
def validateName(name_input):
    '''This function will validate whether the name entered is made of letters only and is already in the list'''
    if name_input.isalpha() is not True:

        print('Names entered must contain letters only')

        name_input = None

        enterName()

    elif name_input in names:

        print('No duplicate names are allowed')

        name_input = None

        enterName()
         
    else:

        addName(name_input)

        name_input = None

        #print(names) 

#Validate the number entered
def validateNum(num_input):
    '''This function will validate the number entered is a number otherwise request a new entry'''
    if num_input.isdigit() is not True:

       print('Input entered must be a digit') 

       addNum()
    
    if num_input.isnumeric() is not True:

       print('Input entered must be a number') 

       addNum()

    newN = int(num_input) 

    if float(newN).is_integer() is not True:

        print('Input entered must be an integer') 

        addNum()

#Add validated name to list      
def addName(name_input):
    '''This function adds the validated name to the list'''
    names.append(name_input) 

    enterName()

#Retrieve initial input
'''The code below will add the initial name to the list'''
name_input = input("Enter a name to add to your shortlist or press enter to continue: ")

if name_input != '':

    validateName(name_input) 

else:

    validateEntKey(name_input)


    
