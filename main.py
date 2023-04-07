import random
import re

class PythonBBNamer:
    def __init__(self):
        pass

    def is_name_list_correct(self):
        correct_names_flag = [True]

        correct_name_regex = r'[^a-zA-Z]'

        # Check that only alphabetical characters were used.
        for name in self.names_list:
            if re.search(correct_name_regex, name):
                correct_names_flag[0] = False

        return correct_names_flag[0]

    def is_amount_of_names_correct(self):
        correct_amount_of_names_flag = [True]

        # More names are being requested than names were provided.
        if self.amount_of_names > len(self.names_list):
            correct_amount_of_names_flag[0] = False

        # Somehow, less than zero names are being requested.
        if self.amount_of_names < 0:
            correct_amount_of_names_flag[0] = False

        # They couldn't even request a number of names.
        if type(self.amount_of_names) != int:
            correct_amount_of_names_flag[0] = False

        return correct_amount_of_names_flag[0]

    # Get the names that they want a literal machine to name their child after.
    def get_names_list(self,):
        self.names_list = input("Enter the names that you want seperated by a space:\n").split(' ')

        if not self.is_name_list_correct():
            print("\nPlease enter valid identifiers for your own child.")
            self.get_names_list()

    # Get the amount of names to be displayed
    def get_amount_of_names(self):
        self.amount_of_names = int(input("how many you want:\n"))

        # Repeat until the amount of names is correct
        if not self.is_amount_of_names_correct():
            print("Please enter a valid number of names to display.")
            self.get_amount_of_names()

    def get_name_suggestions(self):
        name_suggestions = []

        for i in range(self.amount_of_names):
            name_suggestions.append(self.names_list.pop(random.randint(0, len(self.names_list) - 1)))

        return name_suggestions
    

    def intro(self):
        print("So you can't think of a name for your own child.")
        print("This lifeless machine is happy to help :)")

    

def main():

    pytonbbname = PythonBBNamer()

    pytonbbname.intro()
    pytonbbname.get_names_list()
    pytonbbname.get_amount_of_names()
    for name in pytonbbname.get_name_suggestions():
        print(name)


if __name__ == '__main__':
    main()