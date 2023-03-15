import random

print ("Welcome to the random name generator!")

def get_shortlist():
# Reads the names that th user inputs and returns a list.
    shortlist_str = input("Please enter names, separated by commas: ")
    return [name.strip() for name in shortlist_str.split(',')]
    
def get_num_names():
# Reads the number of names to be selected from the list and returns the interger.
  while True: 
    num_names_str = input("Enter the number of names to be selected: ")
    if num_names_str.isdigit():
        return int(num_names_str)
    else:
            print("Invalid input. Please Enter a postive interger.")

def select_names(shortlist, num_names):
# Selects num_names names randomly from the given list and returns a list.
    return random.sample(shortlist, num_names)

if __name__== '__main__':
    shortlist = get_shortlist()
    num_names = get_num_names()

    if num_names > len(shortlist):
        print(f" Please enter the number of names to be selected: ({num_names}) is greater than the number of names in the shortlist ({len(shortlist)}.")
    else:
        selected_names = select_names(shortlist, num_names)
        print(f"Selected names: {','.join(selected_names)}")
        

