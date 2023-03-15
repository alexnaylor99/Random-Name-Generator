# Beginners Python Project - Random Name Generator
Program to choose a random name from a list

## Project Description
- Project written in Python
- Project uses 3 basic functions 
  - input name list
  - identify how many random choices


## Program steps
1. User is asked to input names that they want
    1.1. input_name = Enter random names... 
        1.1.1. name_list.append(input_name)
        1.1.2. name_list_items = len(name_list)
    1.2. return list of names and number of names in list
2. User is asked how many random names to pick from their created list
    2.1. number of names = number *must not exceed {name_list_items}*
    2.2. if number of names < 1 or > number of names in list
        2.2.1. ask number of names again      
    2.3. otherwise save the desired number of random names 
3. Program will show user the names randomly selected
    3.1. select random names from the list by 'number' of names
    3.2. selected names are shown
