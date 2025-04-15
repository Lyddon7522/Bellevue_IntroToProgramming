import unittest
from unittest.mock import patch
import io
from main_m6 import get_numbers, calculate_statistics, find_lowest, find_highest, calculate_total, calculate_average


class TestNumberStatistics(unittest.TestCase):
    
    @patch('builtins.input', side_effect=["1", '10', '20', '30', '40', '50', 
                                                       '15', '25', '35', '45', '55',
                                                       '5', '60', '70', '80', '90',
                                                       '100', '75', '85', '95', '65'])
    def test_get_numbers_manual(self, mock_input):
        """Test that get_numbers collects and returns the correct list of numbers when manually entering them."""
        result = get_numbers()
        expected = [10.0, 20.0, 30.0, 40.0, 50.0, 
                   15.0, 25.0, 35.0, 45.0, 55.0,
                   5.0, 60.0, 70.0, 80.0, 90.0,
                   100.0, 75.0, 85.0, 95.0, 65.0]
        self.assertEqual(result, expected)
        self.assertEqual(len(result), 20)  # Ensure we have 20 numbers
    
    @patch('builtins.input', side_effect=["2"])
    @patch('random.uniform', return_value=42.0)
    def test_get_numbers_random(self, mock_random, mock_input):
        """Test that get_numbers generates random numbers correctly when that option is chosen."""
        result = get_numbers()
        # Since we mocked random.uniform to always return 42.0
        expected = [42.0] * 20
        self.assertEqual(result, expected)
        self.assertEqual(len(result), 20)
        # Verify random.uniform was called 20 times
        self.assertEqual(mock_random.call_count, 20)
    
    @patch('builtins.input', side_effect=["3", "invalid", "1", "abc", "10", "20", "30"])
    @patch('main_m6.range', return_value=range(3))
    def test_input_validation(self, mock_range, mock_input):
        """Test that invalid inputs are handled correctly."""
        # Use a context manager to patch stdout
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            result = get_numbers()
            
            self.assertEqual(result, [10.0, 20.0, 30.0])
            self.assertIn("Invalid choice", mock_stdout.getvalue())
            self.assertIn("Invalid input", mock_stdout.getvalue())
    
    # Tests for the statistics calculations
    def test_find_lowest(self):
        """Test finding the lowest number in a list."""
        numbers = [10, 5, 20, 15, 30]
        self.assertEqual(find_lowest(numbers), 5)
    
    def test_find_highest(self):
        """Test finding the highest number in a list."""
        numbers = [10, 5, 20, 15, 30]
        self.assertEqual(find_highest(numbers), 30)
    
    def test_calculate_total(self):
        """Test calculating the total of the numbers in a list."""
        numbers = [10, 5, 20, 15, 30]
        self.assertEqual(calculate_total(numbers), 80)
    
    def test_calculate_average(self):
        """Test calculating the average of the numbers in a list."""
        numbers = [10, 5, 20, 15, 30]
        self.assertEqual(calculate_average(numbers), 16)
    
    def test_calculate_statistics(self):
        """Test that calculate_statistics returns correct statistics dictionary."""
        numbers = [10, 5, 20, 15, 30]
        stats = calculate_statistics(numbers)
        
        self.assertEqual(stats['lowest'], 5)
        self.assertEqual(stats['highest'], 30)
        self.assertEqual(stats['total'], 80)
        self.assertEqual(stats['average'], 16)


if __name__ == '__main__':
    unittest.main()
