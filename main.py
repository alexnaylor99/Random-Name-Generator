"""
Criteria:
- Take a user input of shortlist names.
- Take a second user input of how many names they want randomly selected from that shortlist. This should be a positive integer. The app should check if the input is valid.
- Print to the user the randomly selected names. 
"""
import random

def select_random_names():
    # Request User to enter a list of names
    shortlist = input("Enter a comma-separated list of names: ").split(",")
    shortlist = [name.strip() for name in shortlist]
    # Request the User to enter the number of names they would like to have randomly selected
    num_names = input("How many names do you want randomly selected? ")
    
    # Check if the input is a positive integer
    try:
        num_names = int(num_names)
        if num_names <= 0:
            raise ValueError("Number of names must be a positive integer.")
    except ValueError as e:
        print("Invalid input:", e)
        return
    
    # Print the randomly selected names
    random_names = random.sample(shortlist, num_names)
    print("Randomly selected names:", ", ".join(random_names))

if __name__ == '__main__':

    select_random_names()



