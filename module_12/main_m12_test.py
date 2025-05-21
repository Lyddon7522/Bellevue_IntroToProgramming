import unittest
from unittest.mock import patch, MagicMock
import json
import sys
import io
import requests
from main_12 import validate_zip_code, get_current_weather_data, display_weather

class TestWeatherApp(unittest.TestCase):

    # Save original stdout
    original_stdout = sys.stdout

    def setUp(self):
        # Restore stdout before each test
        sys.stdout = self.original_stdout

    def tearDown(self):
        # Restore stdout after each test
        sys.stdout = self.original_stdout

    def test_validate_zip_code_valid(self):
        """Test validation with valid zip codes"""
        valid_zips = [
            "12345",      # Standard 5-digit
            "90210",      # Standard 5-digit
            "00000",      # All zeros
            "54321"       # Standard 5-digit
        ]
        for zip_code in valid_zips:
            self.assertTrue(validate_zip_code(zip_code), f"Failed to validate {zip_code}")

    def test_validate_zip_code_invalid(self):
        """Test validation with invalid zip codes"""
        invalid_zips = [
            "1234",       # Too short
            "123456",     # Too long
            "abcde",      # Non-numeric
            "12a45",      # Contains non-numeric
            "",           # Empty string
            " 12345",     # Leading space
            "12345 ",     # Trailing space
            "12345-6789", # 9-digit format with hyphen (no longer valid)
            "12345-123",  # Any hyphenated format
            "12345-",     # Hyphen at end
            "-12345",     # Hyphen at beginning
            "12345 6789"  # Space in middle
        ]
        for zip_code in invalid_zips:
            self.assertFalse(validate_zip_code(zip_code), f"Incorrectly validated {zip_code}")

    @patch('requests.get')
    def test_get_weather_data_success(self, mock_get):
        """Test successful API call to get weather data"""
        # Create a mock response
        mock_response = MagicMock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {
            "name": "Test City",
            "weather": [{"description": "clear sky"}],
            "main": {"temp": 72.5, "feels_like": 70.1, "humidity": 45},
            "wind": {"speed": 5.2}
        }
        mock_get.return_value = mock_response

        # Call the function with test data
        result = get_current_weather_data("12345")

        # Verify the API was called with correct parameters
        mock_get.assert_called_once()
        call_args = mock_get.call_args[1]['params']
        self.assertEqual(call_args["zip"], "12345,us")
        self.assertEqual(call_args["units"], "imperial")

        # Verify the function returns expected data
        self.assertEqual(result["name"], "Test City")
        self.assertEqual(result["weather"][0]["description"], "clear sky")
        self.assertEqual(result["main"]["temp"], 72.5)

    @patch('requests.get')
    def test_get_weather_data_failure(self, mock_get):
        """Test API call failure handling"""
        # Make the request fail
        mock_get.side_effect = requests.exceptions.RequestException("API Error")

        # Use StringIO to capture output
        captured_output = io.StringIO()
        original_stdout = sys.stdout
        sys.stdout = captured_output

        try:
            result = get_current_weather_data("12345")
            # Get the output
            output = captured_output.getvalue()
            # Verify the function handles errors properly
            self.assertIsNone(result)
            self.assertIn("Error fetching weather data", output)
        finally:
            # Always restore stdout even if the test fails
            sys.stdout = original_stdout

    def test_display_weather(self):
        """Test the weather display function"""
        test_data = {
            "name": "Test City",
            "weather": [{"description": "clear sky"}],
            "main": {"temp": 72.5, "feels_like": 70.1, "humidity": 45},
            "wind": {"speed": 5.2}
        }

        # Use StringIO to capture output
        captured_output = io.StringIO()
        original_stdout = sys.stdout
        sys.stdout = captured_output

        try:
            display_weather(test_data)
            # Get the output
            output = captured_output.getvalue()
            # Check that the output contains expected weather information
            self.assertIn("Test City", output)
            self.assertIn("Clear Sky", output)
            self.assertIn("72.5°F", output)
            self.assertIn("70.1°F", output)
            self.assertIn("45%", output)
            self.assertIn("5.2 mph", output)
        finally:
            # Always restore stdout even if the test fails
            sys.stdout = original_stdout

    def test_display_weather_missing_data(self):
        """Test display function with incomplete weather data"""
        test_data = {"name": "Test City"}  # Missing most fields

        # Use StringIO to capture output
        captured_output = io.StringIO()
        original_stdout = sys.stdout
        sys.stdout = captured_output

        try:
            display_weather(test_data)
            # Get the output
            output = captured_output.getvalue()
            # Check that the function handles missing data
            self.assertIn("Test City", output)
            self.assertIn("Unknown", output)
        finally:
            # Always restore stdout even if the test fails
            sys.stdout = original_stdout

if __name__ == "__main__":
    unittest.main()
