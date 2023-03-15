import random  # import random module

# create global variables to store names and number of names
name_list = []
name_list_items = 0
number = 0
selected_name = []


def insert_names():
    '''This function will insert names into the name_list
        input = 'string' --> saved to list['string1', 'string2', 'string3', etc.]
        output = 'list' and len(list)
    '''
    global name_list
    global name_list_items
    while True:
        input_name = input('Enter random names... to STOP press \'c\' : ')
        if input_name == 'c':
            break
        else:
            name_list.append(input_name)
            name_list_items = len(name_list)
    return name_list, name_list_items
    

def number_of_names(name_list_items):
    '''This function will ask for the number of names to be selected
        input = 'int' --> must not exceed the number of names in the list len(name_list_items)
        output = 'int' --> saved to variable 'number'
    '''
    global number
    while True:
        int_number = int(input(f'Enter number of desired names *must not exceed {name_list_items}*: '))
        if int_number < 1 or int_number > name_list_items:
            number = int(input('Input is invalid. Enter again number of desired names: '))      
        else:
            number = int_number
            break


if __name__ == '__main__':
    '''This is will run the program in an order
        1. insert_names() --> will insert names into the name_list
        2. number_of_names(name_list_items) --> will ask for the number of names to be selected from list
        3. random.sample(name_list, number) --> will select random names from the list by 'number' of names
    '''
    insert_names()
    number_of_names(name_list_items)
    selected_name = random.sample(name_list, number)
    print (selected_name)


