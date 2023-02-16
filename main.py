import random

print ("Hello!")
names = input ('Please enter the names separated by a space:')
names = str(names).split ()

names = list(set(names))

random_number = input ('Please enter how many names you would like: ')

name = random.sample (names, k = int(random_number))

#if int(random_number) < 1: 
 #   raise ValueError ("Please enter a positive whole number")
# how do i reset to enter input if error

print ("The name(s) are:",name)

