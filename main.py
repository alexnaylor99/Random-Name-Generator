import random

#function takes two arguments 'num_names, shortlist' which is the number of names to generate and which is the list of names to select from.
def generate_names(num_names, shortlist):
    names = []
#It uses a for loop to randomly select a name from the shortlist
    for i in range(num_names):
        name = random.choice(shortlist)
#append it to the names list
        names.append(name)
#remove it from the shortlist to prevent duplicates
        shortlist.remove(name)
    return names

def main():
#enter a number of names to randomly select from the shortlist
    shortlist = input("Enter names for the shortlist, separated by commas: ").replace(" ", "").split(",")
    num_names = len(shortlist)
    print(f"{num_names} names added to the shortlist.")
    
#checks to make sure the input is valid
    while True:
        num_select = input("How many names do you want to randomly select from the shortlist? ")
        try:
            num_select = int(num_select)
            if num_select <= 0:
                raise ValueError
            if num_select > num_names:
                raise IndexError
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
        except IndexError:
            print(f"Invalid input. There are only {num_names} names in the shortlist.")

#calls the generate_names function to generate the specified number of names  
    names = generate_names(num_select, shortlist)

#prints out the selected names using the join method to combine the list into a string separated by commas
    print(f"Randomly selected names: {', '.join(names)}")

if __name__ == "__main__":
    main()