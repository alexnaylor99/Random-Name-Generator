'''The program will prompt the user to enter a name to add to the shortlist, or press Enter to continue. 
Once the user has entered at least two names, they can choose to generate a random selection of names from the list by entering a number between 1 and the length of the list.'''

import random
import re

num_input = 0

names = set()

def addNames():

    '''This function allows the user to continuously add names to the list.'''
    user_input = None
    while user_input != '':
        user_input = input("Using only letters enter names to add to your shortlist, duplicates will be ignored: ")
        if user_input != '':
            names.add(user_input)
        while user_input == '' and len(names) == 0:
            user_input = input("Please enter at least one name: ")
            if user_input != '':
                names.add(user_input)
        else:
            while user_input != '':
                user_input = input("Add more names or press enter to stop: ")
                
                if user_input != '':
                    names.add(user_input)

            else:
                if len(names) == 1:
                    addMore = input("you only have one name in your list, the output will be very predictable, would like to add more names? Y or N: ") 
                    while re.match("[^YNyn]", addMore):
                        addMore = input("That is not a valid input please enter Y for yes and N for no, input is case insensitive: ")
                    else:
                        if addMore == 'Y' or addMore == 'y':
                            addNames()
                        elif addMore == 'N' or addMore == 'n':
                            return addNumber()
                        
                else:
                    return addNumber()

    return addNumber();

def addNumber():
    '''This function allows the user to select how many random outputs they would like to generate'''
    num_input = input(f"Enter a number between 1 and {len(names)}: ")

    newN = int(num_input)

    while newN > len(names) or newN <= 0:
        num_input = input(f"Number entered must be between 1 and {len(names)} inclusive: ")
        
        newN = int(num_input)

    else:
        newN = int(num_input)

        indices = []

        for i in range(newN):

            #rNum = None
            def newNum():
                rNum = random.randint(1, len(names))

                while rNum in indices:
                    rNum = random.randint(1, len(names))
                else:
                    return rNum
                
            indices.append(newNum())
            
            #print(indices)

        output = []

        for j in indices:
            nameList = list(names)
            output.append(nameList[j-1])
            #print(nameList[j-1])
           
        return output

print(addNames())

#print(type(num_input))

#addNames()

