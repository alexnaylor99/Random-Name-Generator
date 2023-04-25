import random

def random_name_generator():
    # Prompts user to input names and creates a list
    list_of_names = input("Enter a list of names seperated by commas:")
    list_of_names = list_of_names.split(",")
    list_of_names = [i.strip(" ") for i in list_of_names]

    # Prompts user to input number of names he would like
    while True:
        num_of_names = input("Enter the number of names you would like:")
        if not num_of_names.isdigit() or len(list_of_names) < int(num_of_names) or int(num_of_names) <= 0:
            print("Please enter an integer which is greater than 0 and less than or equal to the number number of names you have added")
            continue
        else:
            break
    
    # If conditions are met, names are then given
    num_of_names = int(num_of_names) 
    selected_names = random.sample(list_of_names, num_of_names)
    print("Here are your names:")
    for name in selected_names:
        print(name)
    return random_name_generator()

random_name_generator()
