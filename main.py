import random

def Names():
    """
    The function asks the user for names, checks them, and returns them.
    """
    name_list = input("Please put in a list of names separated by spaces: ")
    name_list_final = list(set(name_list.split()))

    while len(name_list_final) < 2:
        name_list = input("Please input more than one name please. ")
        name_list_final = list(set(name_list.split()))

    return name_list_final
    
def Number(name_list_final):
    """ 
    This function will ask the user the number of names they want from the list
    """
    while True:
        
        try:
            number_of_names = int(input(f"How many names would you like? Min:1 Max: {len(name_list_final)}"))
            if 1 <= number_of_names <= len(name_list_final):
                return number_of_names

        except ValueError:
            print("Please insert a correct number. (eg 1, 2, 3, 4...)")
            
def Random_Name(names,number):
    random_names = random.choices(names,k=number)
    print(f"Random names are {random_names}")

            
