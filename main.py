#a function that takes a list of names and a number as arguments
#the function should return x number of names randomly

import random

def random_name_generator(list_names, num_of_names):
    shortlist = random.choices(list_names, k=num_of_names)
    return shortlist

