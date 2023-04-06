import random;
names = []
#A user-defined function that collects names from the user to create a shortlist and verifies user input
def namePicker():
    numNames = input("How many names would you like to enter?\n")
    
    if(numNames.isnumeric()):#is numeric is used to check if the user has entered a string that has numeric format.
        i = 0
        while i < int(numNames): #for i in range(numNames) may be an alternative to achieve this.
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
    return names,numNames


#A user-defined function that verifies user input and checks how many names to pick randomly
def noOfRandName(selectRange):
    noOfNames = input('How many random names would you like to generate from the shortlist\n');
    if(noOfNames.isnumeric() and noOfNames < selectRange):
        selector(int(selectRange),int(noOfNames))
    elif(noOfNames.isnumeric() and noOfNames > selectRange):
        print('The shortlist of names you provided does not have that many names')
    else:
        print('Please provide valid numeric input')

#A user-defined function that uses Python's random package to select the names from the shortlist.
def selector(max, noOfNames):
    i = 0
    resultNames = []
    while i < noOfNames:
        randNo = random.randint(0,max - 1)
        if names[randNo] not in resultNames:
            resultNames.append(names[randNo])
            i += 1
            
    print(resultNames)
    
nameChoice = namePicker()
noOfRandName(nameChoice[1])

