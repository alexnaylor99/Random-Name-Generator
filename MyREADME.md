# Random Name Selector Readme

This Python program allows the user to create a shortlist of names and generate a random selection from that list. The program prompts the user to enter names one by one until they choose to stop. Once the user has entered at least two names, they can choose to generate a random selection of names from the list.

## Installation

No installation is required. The program can be run on any machine with Python 3 installed.

## Dependencies

- This code requires Python 3.x.
- The random module is used to select random names from the list.

## Usage

To use the program, navigate to the directory where the file is located and run it using Python in the terminal or command prompt:

- Run the script in the terminal or command line "python main-option-2.py".
- Follow the prompts to enter names into the list.
- When ready to select random names, enter a number between 1 and the length of the name list.
- The program will randomly select the specified number of names from the list and display the results.

## Functions

- addNum()
This function prompts the user to enter a number between 1 and the length of the name list. It validates that the user input is a valid integer and within the range of the list. Then it uses the random module to select a specified number of unique names from the list and returns the results.

- enterName()
This function prompts the user to enter a name into the list. It validates that the input only contains letters and does not already exist in the list.

- validateEntKey(name_input)
This function validates the user input when they press the enter key. If the list only contains one name, it will prompt the user to enter another name. Otherwise, it will call the addNum() function to randomly select names.

- validateName(name_input)
This function validates the user input for adding a name to the list. It checks that the input only contains letters and does not already exist in the list. If the input is valid, it adds the name to the list and calls the enterName() function to continue prompting the user for input.

- validateNum(num_input)
This function validates the user input when entering the number of names to select. It checks that the input is a valid integer.

- addName(name_input)
This function adds the validated user input to the list of names and calls the enterName() function to continue prompting the user for input.

## Example

Enter a name to add to your shortlist or press enter to continue: Alice

Enter a name and press enter to add it to the list otherwise just press enter to stop: Bob

Enter a name and press enter to add it to the list otherwise just press enter to stop: Charlie

Enter a name and press enter to add it to the list otherwise just press enter to stop: 

continue

Enter a number between 1 and 3: 2

['Charlie', 'Alice']

## License
This program is licensed under the MIT License. Feel free to use, modify, and distribute it as you see fit. See the LICENSE file for details.
