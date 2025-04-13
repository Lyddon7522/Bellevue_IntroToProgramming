import unittest
import os
import tempfile
from unittest.mock import patch
from main_m5 import (
    is_valid_address_format, 
    is_valid_phone_format, 
    write_to_csv, 
    read_csv_file, 
    User, 
    get_filename
)


class InputValidationTests(unittest.TestCase):
    def test_valid_address_formats(self):
        """Test that valid address formats are accepted."""
        valid_addresses = [
            "123 Main St",
            "456 Elm Avenue, Apt 7B",
            "789 Oak Dr, Springfield, IL 62701",
            "1010 5th Ave, New York, NY 10018",
            "42 Wallaby Way, Sydney"
        ]
        
        for address in valid_addresses:
            with self.subTest(address=address):
                self.assertTrue(is_valid_address_format(address), 
                               f"Address should be valid: {address}")

    def test_invalid_address_formats(self):
        """Test that invalid address formats are rejected."""
        invalid_addresses = [
            "",  # Empty string
            "123",  # Just a number
            "Main St",  # No street number
            "@@##$$",  # Invalid characters only
            "AB"  # Too short
        ]
        
        for address in invalid_addresses:
            with self.subTest(address=address):
                self.assertFalse(is_valid_address_format(address), 
                                f"Address should be invalid: {address}")
    
    def test_valid_phone_formats(self):
        """Test that valid phone formats are accepted."""
        valid_phones = [
            "123-456-7890",
            "800-555-1212",
            "555-123-4567"
        ]
        
        for phone in valid_phones:
            with self.subTest(phone=phone):
                self.assertTrue(is_valid_phone_format(phone), 
                               f"Phone should be valid: {phone}")

    def test_invalid_phone_formats(self):
        """Test that invalid phone formats are rejected."""
        invalid_phones = [
            "",  # Empty string
            "1234567890",  # No hyphens
            "123-456-789",  # Too few digits
            "123-456-78901",  # Too many digits
            "12-345-6789",  # Wrong format
            "123-45-6789",  # Wrong format
            "abc-def-ghij"  # Letters instead of numbers
        ]
        
        for phone in invalid_phones:
            with self.subTest(phone=phone):
                self.assertFalse(is_valid_phone_format(phone), 
                               f"Phone should be invalid: {phone}")


class FileOperationsTests(unittest.TestCase):
    def setUp(self):
        """Create a temporary directory for test files."""
        self.test_dir = tempfile.TemporaryDirectory()
        self.test_file_path = os.path.join(self.test_dir.name, "test_output.csv")
        self.test_user = User("John Doe", "123 Main St", "555-123-4567")

    def tearDown(self):
        """Clean up temporary directory after tests."""
        self.test_dir.cleanup()

    def test_write_to_csv(self):
        """Test that data is correctly written to a CSV file."""
        # Write data to the test file
        write_to_csv(self.test_file_path, self.test_user)
        
        # Verify the file exists
        self.assertTrue(os.path.exists(self.test_file_path), 
                        "CSV file should be created")
        
        # Read the content and verify
        with open(self.test_file_path, 'r') as f:
            content = f.read()
            self.assertIn("Name,Address,Phone Number", content, 
                          "CSV should have headers")
            self.assertIn("John Doe,123 Main St,555-123-4567", content, 
                          "CSV should contain user data")

    def test_read_csv_file(self):
        """Test that data is correctly read from a CSV file."""
        # First write some data
        write_to_csv(self.test_file_path, self.test_user)
        
        # Then read it back
        rows = read_csv_file(self.test_file_path)
        
        # Verify the data was read correctly
        self.assertIsNotNone(rows, "Should return rows data")
        self.assertEqual(len(rows), 2, "Should have header row and data row")
        self.assertEqual(rows[0], ['Name', 'Address', 'Phone Number'], 
                         "First row should be headers")
        self.assertEqual(rows[1], ['John Doe', '123 Main St', '555-123-4567'], 
                         "Second row should be user data")
        
    def test_read_nonexistent_file(self):
        """Test reading a file that doesn't exist."""
        nonexistent_file = os.path.join(self.test_dir.name, "nonexistent.csv")
        result = read_csv_file(nonexistent_file)
        self.assertIsNone(result, "Should return None for nonexistent file")


class FilenameProcessingTests(unittest.TestCase):
    @patch('builtins.input', return_value='testfile')
    def test_filename_without_extension(self, mock_input):
        """Test that .csv extension is added when not provided."""
        filename = get_filename()
        self.assertEqual(filename, 'testfile.csv', 
                        "Should add .csv extension")
    
    @patch('builtins.input', return_value='testfile.csv')
    def test_filename_with_extension(self, mock_input):
        """Test that extension is not added when already provided."""
        filename = get_filename()
        self.assertEqual(filename, 'testfile.csv', 
                        "Should not change filename with extension")
    
    @patch('builtins.input', return_value='testfile.CSV')
    def test_filename_with_uppercase_extension(self, mock_input):
        """Test that case is handled correctly in extensions."""
        filename = get_filename()
        self.assertEqual(filename, 'testfile.CSV', 
                        "Should not change filename with uppercase extension")


class UserClassTests(unittest.TestCase):
    def test_user_class(self):
        """Test User class functionality."""
        # Create a user
        user = User("Jane Smith", "456 Oak Ave", "123-456-7890")
        
        # Test attributes
        self.assertEqual(user.name, "Jane Smith")
        self.assertEqual(user.address, "456 Oak Ave")
        self.assertEqual(user.phone, "123-456-7890")
        
        # Test string representation
        self.assertEqual(str(user), "Jane Smith, 456 Oak Ave, 123-456-7890")


if __name__ == '__main__':
    unittest.main()
