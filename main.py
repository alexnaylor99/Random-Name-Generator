
import random

def init():
    #Prompts user to input a list of names separated by a space
    user_input = input("Enter your shortlisted names separated by a space:\n")

    #This empty list will be used to separate user input and store each name as an element 
    shortlist = []

    #Iterates over the space separated user input and appendse each name to a list 
    for name in user_input.split(" "):
        shortlist.append(name)

    #Prompts the user to input the desired number of name suggestions
    #The input is then converted to an int for further processing
    choices = int(input("Enter the number of suggestions you would like:\n"))

    #Checks that the user provided a positive int and a number that doesn't exceed the provided names
    while(choices <= 0 or choices > len(shortlist)):
        print("Error! Your input must be a positive integer and not less than the number of input names")
        choices = int(input("Enter the number of suggestions you would like:\n"))

    # random_i = [random.randint(1,len(shortlist)-1) for _ in range(1,choices+1)]

    #Create a list of randomly generated numbers with a specified range
    sample = random.sample(range(1,len(shortlist)-1), choices)
    for i in sample:
        #Print the suggested names back to the user
        print(shortlist[i])


init()

