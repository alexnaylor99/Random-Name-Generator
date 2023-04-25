import random

# Asks user to input the names and format them to remove spaces and store in a list.
input_names = input('Enter a list of names separated by a comma (e.g. "Sam, John, Ben"): ')
names_list = input_names.split(',')
names_list = [name.strip(" ") for name in names_list]

 
while True:
    try:
        # Asks user for an input for the number of names they would like shortlisted.
        num_names = int(input('Enter number of names you would like randomly shortlisted?: '))
        # Ensures the number entered is within the parameters of what has been entered.
        if num_names < 0 or num_names > len(names_list):
            print(f"You must choose a number between 1 and {len(names_list)}. Please enter a valid number considering the number of names inputted")
        else:
            break
    # Allows the loop to continue if anything other than an integer is entered.
    except ValueError:
        print("You have not entered a valid number. Try again")
            

# Takes a random number of names according to the inputs and prints them out.
final_shortlist = random.sample(names_list, num_names)  
print("Your randomly shortlisted names are: ")
for name in final_shortlist:
    print (name.capitalize())

# Furqan Ahmad


