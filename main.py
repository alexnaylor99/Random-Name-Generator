import random
import string

# Sometimes people don't have a list and want a random name generated
predefined_names = ["Kevin", "Christian", "Christopher", "Mario", "Henry", "Alex", "Adam", "Oliver", "Evelyn", "Matthew"
                    , "Yeni", "Masud", "Kseniia", "Sumaya", "Shahrukh", "Tariq", "Andrew", "Emmanuel"]

# Prompt the user to enter a list of names or choose from a predefined list
names = input("Enter a list of names (separated by commas), or '#' to select from a predefined list: ")
if names == "#":
    names = predefined_names
else:
    # Remove duplicates and check that each name only contains letters
    names = [name.strip() for name in names.split(',') if name.strip()]
    for name in names:
        if not all(c in string.ascii_letters for c in name):
            print(f"Invalid name: '{name}'. Names can only contain letters. Please try again.")
            exit()

# Make sure the list of names is not empty
if not names:
    print("No names entered. Try again.")
    exit()

# Check that the chosen number of names is more than 1 and is an integer
num_names = input("How many names do you want to select? ")
try:
    num_names = int(num_names)
    if num_names <= 0:
        raise ValueError("Number of names must be positive.")
except ValueError:
    print("Invalid input. Please enter a positive integer.")
    exit()

# Check that the number chosen isn't longer than the list of names
if num_names > len(names):
    print("Number of names to select exceeds number of names entered. Try again.")
    exit()

# Select the specified number of random names from the list
selected_names = random.sample(names, num_names)

# Print the selected names
print("Selected names:")
for name in selected_names:
    # Check that each name is not too long
    if len(name) > 50:
        print(f"Warning: Name '{name}' is too long and has been truncated to 50 characters.")
        name = name[:50]
    print(name)
