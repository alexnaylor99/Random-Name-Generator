# Import the requests library
import requests
import random
import re

# Define the URL for the random word API
url = 'https://random-word-api.herokuapp.com/word'


# Define an empty list, this list will be filled with the provided
# results and used to pick a random name as final suggestion
generated_names = []


# Define a function called "results"
# that takes a URL, a number, and a name as inputs
def results(url, num, name):
    # This loop to repeat the creation and display of
    # names provided a number of times provided by the user
    for i in range(num):
        # API call and cleaning of the result
        api_call = requests.get(url)
        nickname = api_call.text.replace(
            '[', '').replace(']', '').replace('"', '')
        # Show the final results and add it to the
        # generated_names list
        madeup_name = (f"\n{name.title()} {nickname.title()}")
        print(madeup_name)
        generated_names.append(madeup_name)


# This asks the user for a name as starting point
# and check is an acceptabe input
while True:
    name = str(input("Please provide a first name of your choice:\n"))
    if len(name) >= 2 and re.match("^[a-zA-Z]+$", name):
        break
    else:
        print("don't be a fool a give me a real name!")

# This asks the user how many examples want to see,
# making sure the input is an integer
while True:
    num = int(input("How many name example you want me to create for you?\n"))
    if num is not int:
        # Here it calls the function that generate and display the names
        results(url, num, name)
        break
    else:
        print("""Well, I asked you how many username examples
         you want, just give a number please!""")

# This show a random name between the the names generated
if len(generated_names) > 1:
    print(
        f"\n\n\n\nIf you ask me, my favourite is {random.choice(generated_names)}\n\n")
