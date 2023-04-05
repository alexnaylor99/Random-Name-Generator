import random;

names = []
#A user-defined function that collects names from the user to create a shortlist and verifies user input
def namePicker():
    numNames = input("How many names would you like to enter?\n");
    if(numNames.isnumeric()):#is numeric is used to check if the user has entered a string that has numeric format.
        i = 0
        while i < int(numNames):
            name = input("Please enter a name: \n");
            if name is names:
                print('You have already entered this name, please enter a new name?');
            else:
                names.append(name);
            i = i + 1;
    else:
        print('Please provide valid numeric input');
    return names,numNames;


#A user-defined function that verifies user input and checks how many names to pick randomly
def noOfRandName(selectRange):
    noOfNames = input('How many random names would you like to generate from the shortlist\n');
    if(noOfNames.isnumeric()):
            selector(int(selectRange),noOfNames);
    else:
        print('Please provide valid numeric input');

#A user-defined function that uses Python's random package to select the names from the shortlist.
def selector(max, noOfNames):
    resultNames = [];
    for i in range(int(noOfNames) + 1):
        randNo = random.randint(0,max - 1);

        if names[randNo] not in resultNames:
            resultNames.append(names[randNo]);

    
    print(resultNames);
    
nameChoice = namePicker();
names = noOfRandName(nameChoice[1]);