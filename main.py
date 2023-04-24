import random;
names = []
#A user-defined function that collects names from the user to create a shortlist and verifies user input
def name_picker():
    num_names = input("How many names would you like to enter?\n")
    
    if(num_names.isnumeric()):#is numeric is used to check if the user has entered a string that has numeric format.
        i = 0
        while i < int(num_names): #for i in range(numNames) may be an alternative to achieve this.
            name = input("Please enter a name: \n")
            if name.lower() in names:
                name = input('You have already entered this name, please enter a new name:')
                names.append(name.lower())
                i += 1
            else:
                names.append(name.lower())
                i += 1
    else:
        print('Please provide valid numeric input')
    return names,num_names


#A user-defined function that verifies user input and checks how many names to pick randomly
def no_of_randname(select_range):
    no_of_names = input('How many random names would you like to generate from the shortlist\n');
    if(no_of_names.isnumeric() and no_of_names < select_range):
        selector(int(select_range),int(no_of_names))
    elif(no_of_names.isnumeric() and no_of_names > select_range):
        print('The shortlist of names you provided does not have that many names')
    else:
        print('Please provide valid numeric input')

#A user-defined function that uses Python's random package to select the names from the shortlist.
def selector(max, no_of_names):
    i = 0
    result_names = []
    while i < no_of_names:
        rand_no = random.randint(0,max - 1)
        if names[rand_no] not in result_names:
            result_names.append(names[rand_no])
            i += 1
            
    print(result_names)
    
name_choice = name_picker()
no_of_randname(name_choice[1])

