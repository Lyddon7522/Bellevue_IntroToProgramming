import unittest
from unittest.mock import patch, MagicMock
import json
import sys
import os
import requests  # Added this import for the exception classes

# Add the parent directory to sys.path to import main_11
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from module_11.main_11 import validate_zip_code, get_weather_data, API_KEY, BASE_URL

class TestWeatherApp(unittest.TestCase):

    def test_validate_zip_code_valid(self):
        """Test that valid zip codes are correctly validated"""
        self.assertTrue(validate_zip_code("12345"))
        self.assertTrue(validate_zip_code("00000"))
        self.assertTrue(validate_zip_code("99999"))

    def test_validate_zip_code_invalid(self):
        """Test that invalid zip codes are correctly rejected"""
        # Too short
        self.assertFalse(validate_zip_code("1234"))
        # Too long
        self.assertFalse(validate_zip_code("123456"))
        # Non-digits
        self.assertFalse(validate_zip_code("abcde"))
        self.assertFalse(validate_zip_code("123-45"))
        # Empty string
        self.assertFalse(validate_zip_code(""))
        # Whitespace
        self.assertFalse(validate_zip_code("     "))
        # None
        self.assertFalse(validate_zip_code(None))

    @patch('requests.get')
    def test_get_weather_data_success(self, mock_get):
        """Test successful weather data retrieval"""
        # Mock the API response
        mock_response = MagicMock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {
            "coord": {"lon": -122.08, "lat": 37.39},
            "weather": [{"id": 800, "main": "Clear", "description": "clear sky"}],
            "main": {"temp": 75.2, "feels_like": 74.3, "temp_min": 72.0, "temp_max": 77.0}
        }
        mock_get.return_value = mock_response

        # Call the function
        result = get_weather_data("50009")

        # Assertions
        self.assertIsNotNone(result)
        self.assertEqual(result["main"]["temp"], 75.2)
        mock_get.assert_called_once()

        # Verify correct API endpoint and parameters
        args, kwargs = mock_get.call_args
        self.assertEqual(args[0], BASE_URL + "/weather")
        self.assertEqual(kwargs["params"]["zip"], "50009,us")
        self.assertEqual(kwargs["params"]["appid"], API_KEY)
        self.assertEqual(kwargs["params"]["units"], "imperial")

    @patch('requests.get')
    def test_get_weather_data_http_error(self, mock_get):
        """Test weather data retrieval with HTTP error"""
        # Mock the API response with an error
        mock_response = MagicMock()
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Client Error: Not Found")
        mock_get.return_value = mock_response

        # Call the function
        result = get_weather_data("00000")

        # Assertions
        self.assertIsNone(result)
        mock_get.assert_called_once()

    @patch('requests.get')
    def test_get_weather_data_connection_error(self, mock_get):
        """Test weather data retrieval with connection error"""
        # Mock a connection error
        mock_get.side_effect = requests.exceptions.ConnectionError("Connection refused")

        # Call the function
        result = get_weather_data("12345")

        # Assertions
        self.assertIsNone(result)
        mock_get.assert_called_once()

if __name__ == '__main__':
    unittest.main()
