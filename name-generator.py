import random

# Function to randomly select a specified number of names from a list of names
def random_name_selector(names, num_selections):
    # Check if the number of selections is valid (greater than 0 and less than or equal to the number of names)
    if num_selections > 0 and num_selections <= len(names):
        # Randomly select the specified number of names
        selected_names = random.sample(names, num_selections)
        return selected_names
    else:
        # Return an error message if the number of selections is invalid
        return "Invalid input: number of selections should be between 1 and the length of the shortlist."

# Main function to handle user input and output
def main():
    # Take user input for shortlist names
    shortlist_names = input("Enter shortlist names separated by a comma: ")
    # Create a list of names by splitting the input string and removing extra spaces
    names_list = [name.strip() for name in shortlist_names.split(',')]

    # Take user input for the number of names to be selected
    while True:
        try:
            num_names = int(input("Enter the number of names you want randomly selected from the shortlist: "))
            # Exit the loop when a valid positive integer is provided
            break
        except ValueError:
            # Display an error message if the input is not a positive integer
            print("Invalid input: Please enter a positive integer.")

    # Call the random_name_selector function with the list of names and the number of selections
    selected_names = random_name_selector(names_list, num_names)
    # Check if the function returned a list of names
    if isinstance(selected_names, list):
        # Print the randomly selected names if the function returned a list
        print(f"Randomly selected names: {', '.join(selected_names)}")
    else:
        # Print the error message if the function did not return a list
        print(selected_names)

# Call the main function to run the code
if __name__ == "__main__":
    main()