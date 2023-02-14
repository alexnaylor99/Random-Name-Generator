"""
Pick random names from a list of names. User enters a names and number to pick.
"""
from random import sample


def get_names() -> set[str]:
    """Return set of names from user input"""

    names = set()
    while True:
        name = input("Enter a name (blank to quit): ")
        if not name:
            break
        names.add(name)
    return names


def get_num_names(max_names: int) -> int:
    """Get number from user input. Must be less than max_names and at least 1."""

    while True:
        num_names = input("Enter number of names to pick: ")
        if num_names.isdigit():
            if int(num_names) > max_names:
                print(f"Number of names must be less than {max_names}")
            elif int(num_names) < 1:
                print("Number of names must be at least 1")
            else:
                return int(num_names)
        else:
            print("Invalid number of names")


def main() -> None:
    """Main function"""

    # Get list of names from user input
    names: set[str] = get_names()

    # Ask user for how many names they want
    num_names: int = get_num_names(len(names))

    # Print the names (sample from tuple as sampling on a set is not supported in 3.9+)
    # Change grammar based on if more than one name selected
    if num_names > 1:
        noun = "names"
        verb = "are:"  # List is started by a colon
    else:
        noun = "name"
        verb = "is"  # No colon needed for a single name

    print(f"The random {noun} {verb} {', '.join(sample(tuple(names), num_names))}")
