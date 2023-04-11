# imported the 'randomize' package
import random

# This is the main function where all functions will be carried out through


def main():
    print(random_sample(input_list(), number_people()))

# This input_list function carries out the functionality to input your names into a list from the user,
# and contains an error check function


def input_list():
    short_list = input("Please type the names into the list: \n").split(" ")
    return non_letters(short_list)

# The non_letters function filers out any typos with the list from the user,
# this includes any character on the keyboard that is not in the alphabet


def non_letters(short_list):
    update_list = []
    for name in short_list:
        update_name = ""
        for letter in name:
            if letter.isalpha():
                update_name += letter
            else:
                continue
        update_list.append(update_name)
    return update_list


# The number_people function is to allow the user to type and pick the amount of names they want from the starting list,
# into the new randomized list, and contains an error check function within


def number_people():
    num_people = 0
    while num_people == 0:
        people = input("How many people would you like to select? \n")
        num_people = is_positive_integer(people)
    return num_people

# The is_positive_integer function is used to varify if the user has typed in a positive integer


def is_positive_integer(number):
    if number.isnumeric():
        if int(number) != 0:
            number = int(number)
            return number
        else:
            print("You can't type 0\n")
            return 0
    else:
        print("Please type in a positive whole number\n")
        return 0

# The random_sample function is used to create and randomize the new list using the users values inputted


def random_sample(original_list, num_people):
    new_list = random.sample(original_list, num_people)
    return "Here is your random sample list: \n" + str(new_list)

# This calls the main function

main()




