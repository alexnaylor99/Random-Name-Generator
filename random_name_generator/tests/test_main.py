"""
Test the main module.
"""
import unittest

from random_name_generator.main import num_names_is_valid, parse_names


class TestParseNames(unittest.TestCase):
    """Test the parse_names function."""

    def test_empty_line(self) -> None:
        """Test ValueError is raised when line is empty."""

        with self.assertRaises(ValueError):
            set(parse_names(""))

    def test_single_name(self) -> None:
        """Test single name is parsed correctly."""

        line = "Alice"
        expected_names = {"Alice"}
        self.assertSetEqual(set(parse_names(line)), expected_names)

    def test_multiple_names(self) -> None:
        """Test multiple names are parsed correctly."""

        line = "Alice, Bob,  Charlie, "
        expected_names = {"Alice", "Bob", "Charlie"}
        self.assertSetEqual(set(parse_names(line)), expected_names)

    def test_multiple_commas(self) -> None:
        """Test multiple commas are parsed correctly."""

        line = "Alice,,Bob,Charlie,"
        expected_names = {"Alice", "Bob", "Charlie"}
        self.assertSetEqual(set(parse_names(line)), expected_names)


class TestNumNamesIsValid(unittest.TestCase):
    """Test the num_names_is_valid function."""

    def test_num_names_is_valid(self) -> None:
        """Test num_names_is_valid function."""

        self.assertTrue(num_names_is_valid(3, 5))  # Expected output: True
        self.assertTrue(num_names_is_valid(1, 10))  # Expected output: True
        self.assertFalse(num_names_is_valid(6, 5))  # Expected output: False
        self.assertFalse(num_names_is_valid(0, 10))  # Expected output: False
        self.assertFalse(num_names_is_valid(-3, 5))  # Expected output: False


if __name__ == "__main__":
    unittest.main()
