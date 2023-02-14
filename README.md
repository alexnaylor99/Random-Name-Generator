# Over-engineered Random Name Generator
> A name generator for the 21st century

## Usage

Ensure you have Python 3.10 or later installed.

Download this directory and run RandomNameGenerator as a module:

```bash
python -m random_name_generator
```

If you have poetry installed, you can also run the program with:

```bash
poetry run python -m random_name_generator
```

Enter a series of names, one per line, then enter a blank line when done. Enter an interger to specify the number of names to generate. The program will then generate that many names and print them to the console.

## Contributing

Ensure you have Poetry installed. To install the dependencies, run:

```bash
poetry install
```

To format with black, run:

```bash
poetry run black .
```

To lint with mypy, run:

```bash
poetry run mypy . --strict
```

To run pylint, run:

```bash
poetry run pylint random_name_generator
```

## Versioning

This project uses [SemVer](http://semver.org/) for versioning.

## Licence

Code is released under the [AGPL version 3](LICENCE).