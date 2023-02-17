import random

print("Hello!")

while True:
    try:
        names = input("Please enter the names separated by a space:").split()

        if len(names) == 0:
            print("Please enter a name")
            raise ValueError()

    except:
        pass
    else:
        break


def RNG():
    global names
    nameslist = list(set(names))
    while True:
        try:
            random_number = input("Please enter how many names you would like: ")

            name = random.sample(nameslist, k=int(random_number))

            if int(random_number) == 0:
                print("Please enter a how many names you would like")
                raise ValueError()

            print("The name(s) are:", name)

        except:
            pass
        else:
            break


RNG()
