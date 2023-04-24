"""name = input("Enter random names with a space: ").split(' ')"""
name = ['ad', 'da w', 'dawwa']
name_list = []
for n in name:
    if n.isalpha():
        name_list.append(n)
print(name_list)