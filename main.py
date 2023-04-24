import random

def input_name():
    name = input("Please enter alpha names with a space in between: ").split(' ')
    name_list = []
    for n in name:
        if n.isalpha():
            print(f"{n} is now added into the database, thanks for entering the name! ")
            name_list.append(n)
    return name_list

def input_length(name_list):
    name_times = input(f"How many names do you want randomly selected from the database? Min: 1, Max: {len(name_list)}\nanswer: ")
    if not name_times.isnumeric() or int(name_times) == 0:
        print("Please enter a valid number that is greater than 0.  ")
        input_length(name_list)
    elif int(name_times) > len(name_list):
        print(f"Please enter a number that equal or lower than {len(name_list)}. ")
        input_length(name_list)
    else:
        print("Thank you, the app will generate random names now. ")
        return int(name_times)

def print_names(name_list, name_times):
    if len(name_list) == 1:
        print("Only one name is selected")
    else:
        random_names = random.sample(name_list, name_times)
        print(f"Random names are {random_names}, thanks for using the app. ")

if __name__ == "__main__":
    name_list = input_name()
    name_times = input_length(name_list)
    print_names(name_list, name_times)