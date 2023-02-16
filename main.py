import random  # import random module

# create variables to store names and number of names
name_list = []
name_list_items = 0
number = 0
selected_name = []

def insert_names():
    '''This function will insert names into the name_list'''
    global name_list
    global name_list_items
    while True:
        input_name = input('Enter random names... to STOP press \'c\' : ')
        name_list.append(input_name)
        if input_name == 'c':
            name_list.remove('c')
            name_list_items = len(name_list)
            return name_list, name_list_items
    

def number_of_names():
    '''This function will ask for the number of names to be selected'''
    global number
    while True:
        number = int(input(f'Enter number of desired names *must not exceed {name_list_items}*: '))
        if number < 1 :
            while True:
                number = int(input('Input in invalid. Enter again number of desired names: '))
                if number >= 1:
                    return number
        return number

   
def random_name_selector():
    '''This function will select random names from the name_list'''
    global selected_name
    for x in range(number):
        selected_name.append(random.choice(name_list))
        if selected_name.count(selected_name[x]) > 1:
            selected_name.remove(selected_name[x])
            selected_name.append(random.choice(name_list))
    return selected_name



if __name__ == '__main__':
    '''This is will run the program in an order'''
    insert_names()
    number_of_names()
    random_name_selector()
    print(selected_name)

