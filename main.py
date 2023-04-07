import random

# Sometimes people don't have a list and want a random name generated
predefined_names = ["Kevin", "Christian", "Christopher", "Mario", "Henry", "Alex", "Adam", "Oliver", "Evelyn", "Matthew"
                    , "Yeni", "Masud", "Kseniia", "Sumaya", "Shahrukh", "Tariq", "Andrew", "Emmanuel"]
names = input("Enter a list of names (separated by commas), or '#' to select from a predefined list: ")
if names == "#":
    names = predefined_names
else:
    names = names.split(',')

# Makes sure the initial input isn't blank
if not any(names):
    print("No names entered. Try again.")
    exit()

# Makes sure the chosen number of names is more than 1
num_names = input("How many names do you want to select? ")
try:
    num_names = int(num_names)
    if num_names <= 0:
        raise ValueError("Number of names must be positive.")
except ValueError:
    print("Invalid input. Please enter a positive integer.")
    exit()

# Makes sure the number chosen isn't longer than the list of names
if num_names > len(names):
    print("Number of names to select exceeds number of names entered. Try again.")
    exit()

selected_names = random.sample(names, num_names)

print("Selected names:")
for name in selected_names:
    print(name)