import random

short_list = input("Please type the names into the list: \n").split(" ")

is_number = False
number_of_people = ""

while not is_number:
    number_of_people = input("How many people would you like to select? \n")
    if number_of_people.isnumeric():
        number_of_people = int(number_of_people)
        is_number = True
    else:
        continue

new_list = random.sample(short_list, number_of_people)
print("Here is your random sample list: \n" + str(new_list))



