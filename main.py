import random


def main():
    print(random_sample(input_list(), number_people()))


def input_list():
    short_list = input("Please type the names into the list: \n").split(" ")
    return short_list


def number_people():
    num_people = 0
    while num_people == 0:
        people = input("How many people would you like to select? \n")
        num_people = is_positive_integer(people)
    return num_people


def is_positive_integer(number):
    if number.isnumeric():
        if int(number) != 0:
            number = int(number)
            return number
    return 0


def random_sample(original_list, num_people):
    new_list = random.sample(original_list, num_people)
    return "Here is your random sample list: \n" + str(new_list)


main()



