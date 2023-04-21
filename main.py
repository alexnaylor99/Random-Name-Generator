#a function that takes a list of names and a number as arguments
#the function should return x number of names randomly

import random
'''
Function description

Parameters
----------
list_names : list of strings
num_names : integer

Returns
-------
Function returns a list of names
'''
def random_name_generator(list_names, num_names):
    shortlist = random.choices(list_names, k=num_names)
    return shortlist

if __name__ == '__main__':
    names = input('Enter a list of names that you are choosing from: ')
    list_names = names.split()
    while True:
        try:
            num_names = int(input('How many names do you want: '))
            if num_names <= 0:
                print('You must choose a number greater than 0. Try again')
                continue
            break
        except Exception as e:
            print(f'Error: {e}\nTry again')
    shortlist = ''
    if len(list_names) > num_names:
        shortlist = random_name_generator(list_names, num_names)
    elif len(list_names) == num_names:
        shortlist = list_names
    else:
        print('There aren\'t enough names on the list!')
    if shortlist:
        print('Here is your shortlist:')
        for count, name in enumerate(shortlist, 1):
            print(f'{count}. {name}')