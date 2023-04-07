import random
import re

class PythonBBNamer:
    """Module for the indecisive parent that can't flip a coin to name their child.
    
    Particularly, people that already have a list of names and can't choose one, but would
    would like another list with slightly less of the same names, that they would probably
    be unable to choose from as well.
    """

    def is_name_list_correct(self):
        """Ensure the names provided are legal for a human entity."""
        
        correct_name_regex = r'[^a-zA-Z]'

        # Check whether a name was entered at all.
        if len(self.names_list) == 1 and self.names_list[0] == "":
            print("\nPlease enter a name.")
            return False

        # Check that only alphabetical characters were used.
        for name in self.names_list:
            if re.search(correct_name_regex, name):
                print("\nPlease only enter characters")
                return False
            
        return True

    def is_amount_of_names_correct(self):
        """Ensure the parent is not already asking for the impossible."""
        
        correct_amount_of_names_flag = [True]

        # More names are being requested than were provided.
        if self.amount_of_names > len(self.names_list):
            print("\nPlease do not request more names than you have provided.")
            correct_amount_of_names_flag[0] = False

        # Somehow, less than zero names are being requested.
        if self.amount_of_names <= 0:
            print("\nPlease request more than 0 names.")
            correct_amount_of_names_flag[0] = False

        # They couldn't even request a number of names.
        if type(self.amount_of_names) != int:
            print("\nPlease enter a digit rather than a character")
            correct_amount_of_names_flag[0] = False

        return correct_amount_of_names_flag[0]

    def get_names_list(self,):
        """Get the names that the parent cannot decide upon"""
        
        self.names_list = input("Enter the names that you want, seperated by a space below\nEg: Chris Christopher ChrisJnr:\n").split(' ')

        # Recursively check whether the entered names are valid.
        if not self.is_name_list_correct():
            # print("\nPlease enter valid identifiers for your child.")
            self.get_names_list()

    # Get the amount of names to be displayed
    def get_amount_of_names(self):
        """Get the amount of names to display"""
        
        self.amount_of_names = int(input("\nHow many you names do you want to choose from:\n"))

        # Recursively check whether the enter number is valid.
        if not self.is_amount_of_names_correct():
            # print("Please enter a valid number of names to display.")
            self.get_amount_of_names()

    def get_name_suggestions(self):
        """Return a random selection of elements from the valid names provided 
        without replacement. The returned selection sized is supplied."""

        name_suggestions = []

        for i in range(self.amount_of_names):
            name_suggestions.append(self.names_list.pop(
                random.randint(0, len(self.names_list) - 1)))

        return name_suggestions
    

    def intro(self):
        """Introdce the uncreative owner to the program."""
        
        print("So, you can't think of a name for your own child.")
        print("Don't worry, this lifeless machine is happy to help :)\n")

    

def main():

    pytonbbname = PythonBBNamer()

    pytonbbname.intro()
    pytonbbname.get_names_list()
    pytonbbname.get_amount_of_names()
    
    print("\nHere's a shortlist of names:")
    for name in pytonbbname.get_name_suggestions():
        print(f" - {name}")


if __name__ == '__main__':
    main()