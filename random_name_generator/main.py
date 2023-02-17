"""
Pick random names from a list of names. User enters a names and number to pick.
"""
from argparse import ArgumentParser
from collections.abc import Generator
from random import sample


def parse_names(line: str) -> Generator[str, None, None]:
    """Yield names from a line of text."""

    if not line:
        raise ValueError("line cannot be empty")

    if "," in line:
        # Split on each comma and add each name, ignoring any empty names
        yield from (csv.strip() for csv in line.split(",") if csv.strip())
    else:
        yield line.strip()


def get_names() -> set[str]:
    """Return set of names from user input."""

    names: set[str] = set()

    # Loop until user enters a blank line
    while True:
        line = input(
            "Enter one name per line or comma-separated (blank to quit): "
        ).strip()
        if not line:
            break
        names.update(parse_names(line))

    return names


def num_names_is_valid(num_names: int, max_names: int) -> bool:
    """Check if num_names is valid."""

    if num_names > max_names:
        print(f"Number of names must be less than {max_names+1}")
        return False

    if num_names < 1:
        print("Number of names must be at least 1")
        return False

    return True


def get_num_names(max_names: int) -> int:
    """Get number from user input. Must be less than max_names and at least 1."""

    if max_names < 1:
        raise ValueError("max_names must be at least 1")

    while True:
        num_names = input("Enter number of names to pick: ").strip()
        if num_names.isdigit():
            if num_names_is_valid(int(num_names), max_names):
                return int(num_names)
        else:
            print("Input must be a positive whole number")


def main() -> None:
    """Main function"""

    parser = ArgumentParser(
        description="Generate a list of random names from a pre-defined shortlist."
    )
    parser.add_argument(
        "--num-names", type=int, help="Number of random names to generate."
    )
    parser.add_argument(
        "--names", type=str, help="File containing the list of names, one per line."
    )
    args = parser.parse_args()

    # If no name file is specified, ask user for names
    if not args.names:
        names: set[str] = get_names()
    else:
        # Load shortlist from file
        with open(args.names, encoding="utf-8") as file:
            names = {name for line in file for name in parse_names(line)}
        if not names:
            print("No names entered")
            return

    # If no number of names is specified, ask user for number
    if not args.num_names:
        num_names: int = get_num_names(len(names))
    else:
        num_names = args.num_names
        if not num_names_is_valid(num_names, len(names)):
            print("Invalid number of names passed to script; enter valid number.")
            num_names = get_num_names(len(names))

    # Change grammar based on if more than one name selected
    if num_names > 1:
        noun = "names"
        verb = "are:"  # List is started by a colon
    else:
        noun = "name"
        verb = "is"  # No colon needed for a single name

    # Print the names (sample from tuple as sampling on a set is not supported in 3.9+)
    print(f"The random {noun} {verb} {', '.join(sample(tuple(names), num_names))}")
