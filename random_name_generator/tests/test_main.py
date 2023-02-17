"""
Test the main module.
"""
from unittest import TestCase, main
from unittest.mock import patch

from random_name_generator.main import get_num_names, num_names_is_valid, parse_names


class TestParseNames(TestCase):
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


class TestNumNamesIsValid(TestCase):
    """Test the num_names_is_valid function."""

    def test_num_names_is_valid(self) -> None:
        """Test num_names_is_valid function."""

        self.assertTrue(num_names_is_valid(3, 5))  # Expected output: True
        self.assertTrue(num_names_is_valid(1, 10))  # Expected output: True
        self.assertFalse(num_names_is_valid(6, 5))  # Expected output: False
        self.assertFalse(num_names_is_valid(0, 10))  # Expected output: False
        self.assertFalse(num_names_is_valid(-3, 5))  # Expected output: False


class TestGetNumNames(TestCase):
    """Test the get_num_names function."""

    def test_get_num_names(self) -> None:
        """Test get_num_names function."""

        inputs = ("0\n", "2\n")
        expected_output = 2

        with patch("builtins.input", side_effect=inputs):
            output = get_num_names(max_names=5)

        self.assertEqual(output, expected_output)

    def test_get_num_names_raises_value_error_on_max_names_less_than_1(self) -> None:
        """Test ValueError is raised when max_names is less than 1."""

        with self.assertRaises(ValueError):
            get_num_names(max_names=0)

    def test_get_num_names_validates_input_is_a_positive_whole_number(self) -> None:
        """Test ValueError is raised when input is not a positive whole number."""

        inputs = ("2.5\n", "foo\n", "3\n")
        expected_output = 3

        with patch("builtins.input", side_effect=inputs):
            output = get_num_names(max_names=5)

        self.assertEqual(output, expected_output)

    def test_get_num_names_validates_input_is_less_than_max_names(self) -> None:
        """Test ValueError is raised when input is greater than max_names."""

        inputs = ("6\n", "2\n")
        expected_output = 2

        with patch("builtins.input", side_effect=inputs):
            output = get_num_names(max_names=5)

        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    main()
