import random

names = []


def add_name():
    print('Press x stop entering a name')
    print('Enter a name:')
    while True:
        name = input()

        if name == 'x':
            # Check at least two names have been entered
            if len(names) < 2:
                print("Please enter at least 2 names")
                continue
            break
        # Check that only letters have been entered
        elif name.isalpha():
            names.append(name)
            print("Enter another name: ")
            continue

        print("Please only use letters: [a-zA-Z]. Try again.")


def rand_name_amount():
    print("Enter the number of names you want to select: ")
    while True:
        num_to_select = input()
        # Check if only numbers have been added
        if num_to_select.isdigit():
            # Check 0 hasn't been chosen to randomly pick
            if int(num_to_select) == 0:
                print("Please choose at least one name to be randomly chosen")
                continue
            # Check if the amount desired to pick is not more than the amount of names in the list
            elif int(num_to_select) <= len(names):
                chosen_names = random.choices(names, k=int(num_to_select))
                return print("Chosen names: ", chosen_names)
            print(
                "The amount of names you want to pick is larger than the number names you've inputted. Please try again")
            continue
        print("Please only use numbers. Try again.")


add_name()
rand_name_amount()
