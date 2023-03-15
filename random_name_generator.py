import random

def get_names():
    name_shortlist = []
    print('Please enter the names you want the generator to consider')
    name_input = input().split()

    for i in name_input:
        name_shortlist.append(i)
    
    print(f'these are the names you have entered: {name_shortlist}')
    return name_shortlist 

def get_num_names():
    names = get_names()

    while True:
        print('How many names do you want from the shortlist')
        num_names =int(input())

        if num_names > len(names):
            print('not enough names in shortlist')
            continue
        
        elif num_names < 0:
            print('number must be a positive number')
            continue

        else:
            print(f' the names selceted for you are:{random.sample(names, num_names)}')

        break