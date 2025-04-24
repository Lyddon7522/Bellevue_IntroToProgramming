import unittest
from unittest.mock import patch
from io import StringIO
from main_m7 import get_initials, validate_name, main

class TestNameInitials(unittest.TestCase):
    
    def test_given_full_name_when_get_initials_then_return_initials(self):
        """Test basic functionality of getting initials."""
        self.assertEqual(get_initials("John William Smith"), "J. W. S.")
        self.assertEqual(get_initials("Alice Marie Johnson"), "A. M. J.")
        self.assertEqual(get_initials("Robert James Williams"), "R. J. W.")
    
    def test_given_single_name_when_get_initials_then_return_single_initial(self):
        """Test getting initials for a single name."""
        self.assertEqual(get_initials("John"), "J.")
    
    def test_given_two_names_when_get_initials_then_return_two_initials(self):
        """Test getting initials for two names."""
        self.assertEqual(get_initials("John Smith"), "J. S.")
    
    def test_given_multiple_middle_names_when_get_initials_then_return_all_initials(self):
        """Test getting initials for a name with multiple middle names."""
        self.assertEqual(get_initials("John William James Smith"), "J. W. J. S.")
    
    def test_given_extra_spaces_when_get_initials_then_ignore_extra_spaces(self):
        """Test getting initials with extra spaces in the input."""
        self.assertEqual(get_initials("  John   William  Smith  "), "J. W. S.")
    
    def test_given_varied_case_when_get_initials_then_return_uppercase_initials(self):
        """Test that initials are always uppercase regardless of input case."""
        self.assertEqual(get_initials("john william smith"), "J. W. S.")
        self.assertEqual(get_initials("JOHN WILLIAM SMITH"), "J. W. S.")
        self.assertEqual(get_initials("jOhN wIlLiAm SmItH"), "J. W. S.")
    
    def test_given_valid_names_when_validate_name_then_return_true(self):
        """Test validation of valid names."""
        self.assertTrue(validate_name("John Smith"))
        self.assertTrue(validate_name("J. Smith"))
        self.assertTrue(validate_name("John W. Smith"))
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_given_empty_name_when_validate_name_then_return_false_and_print_error(self, mock_stdout):
        """Test validation of empty names."""
        self.assertFalse(validate_name(""))
        self.assertIn("Error: Name cannot be empty", mock_stdout.getvalue())
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_given_whitespace_name_when_validate_name_then_return_false_and_print_error(self, mock_stdout):
        """Test validation of whitespace-only names."""
        self.assertFalse(validate_name("   "))
        self.assertIn("Error: Name cannot be empty", mock_stdout.getvalue())
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_given_digits_only_name_when_validate_name_then_return_false_and_print_error(self, mock_stdout):
        """Test validation of digit-only names."""
        self.assertFalse(validate_name("123 456"))
        self.assertIn("Error: Name cannot contain only digits", mock_stdout.getvalue())
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_given_non_alphanumeric_name_when_validate_name_then_return_false_and_print_error(self, mock_stdout):
        """Test validation of names without alphanumeric characters."""
        self.assertFalse(validate_name("!@#$%"))
        self.assertIn("Error: Name must contain at least one alphanumeric character", mock_stdout.getvalue())
    
    @patch('builtins.input', side_effect=["", "123 456", "!@#$%", "John Smith"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_given_multiple_invalid_attempts_when_main_then_prompt_until_valid_and_print_initials(self, mock_stdout, mock_input):
        """Test main function with multiple invalid attempts before a valid name."""
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Error: Name cannot be empty", output)
        self.assertIn("Error: Name cannot contain only digits", output)
        self.assertIn("Error: Name must contain at least one alphanumeric character", output)
        self.assertIn("Your initials are: J. S.", output)

if __name__ == '__main__':
    unittest.main()