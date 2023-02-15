import random

names = []


def add_name():
    print('Press x stop entering a name')
    print('Enter a name:')
    while True:
        name = input()
        if name == 'x':
            break
        elif name.isalpha():
            names.append(name)
            print("Enter another name: ")
            continue
        print("Please only use letters: [a-zA-Z]. Try again.")


def rand_name_amount():
    print("Enter the number of names you want to select: ")
    while True:
        num_to_select = input()
        if num_to_select.isdigit():
            chosen_names = random.choices(names, k=int(num_to_select))
            return print("Chosen names: ", chosen_names)
        print("Please only use numbers. Try again.")


add_name()
rand_name_amount()
