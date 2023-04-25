import random

def Names():
    """
    The function asks the user for names, checks them, and returns them.
    """
    #Ask user for names and removes empty spaces
    name_list = input("Please put in a list of names separated by spaces: ")
    name_list_final = list(set(name_list.split()))

    #Checks that there are more than 1 name inputed
    while len(name_list_final) < 2:
        name_list = input("Please input more than one name please. ")

    return name_list_final
    
def Number(name_list_final):
    """ 
    This function will ask the user the number of names they want from the list
    """
    while True:
        
        try: #Will take the number as an intiger otherwise will return an error
            number_of_names = int(input(f"How many names would you like? Min:1 Max: {len(name_list_final)}"))
            if 1 <= number_of_names <= len(name_list_final):
                return number_of_names
        #Try should loop but if it fails this error will kick in
        except ValueError:
            print("Please insert a correct number. (eg 1, 2, 3, 4...)")


def Random_Name(names,number):
    """
    This function will take the inputed names and selected numbers and choose a random name to display
    """
    random_names = random.choices(names,k=number) #storing the ranom choice
    print(f"Random names are {random_names}")

#Calling the function so that they run correctly so you just need to hit run           
names = Names()
number = Number(names)
Random_Name(names,number)
