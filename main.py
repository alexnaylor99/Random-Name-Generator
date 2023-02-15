import random

name_list = []
number = 0
selected_name = []

def insert_names():
    global name_list
    while True:
        input_name = input('Enter random names... to STOP press \'c\' : ')
        name_list.append(input_name)
        if input_name == 'c':
            name_list.remove('c')
            break
    return name_list


def number_of_names():
    global number
    while True:
        number = int(input('Enter number of desired names: '))
        if number < 1 :
            number = int(input('Enter number of desired names: '))
            return number
        return number

   
def random_name_selector():
    global selected_name
    for x in range(number):
        selected_name.append(random.choice(name_list))
    return selected_name


insert_names()
print(name_list)
number_of_names()
random_name_selector()
print(selected_name)


