import unittest
from unittest.mock import patch
from io import StringIO
from main_m8 import get_stock_price, display_stock_info, main

class TestStockTickerLookup(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures, including a test stock dictionary."""
        self.test_stocks = {
            "AAPL": {"price": 198.45, "name": "Apple Inc.", "last_updated": "2025-05-04"},
            "MSFT": {"price": 425.22, "name": "Microsoft Corporation", "last_updated": "2025-05-04"},
            "AMZN": {"price": 182.15, "name": "Amazon.com Inc.", "last_updated": "2025-05-04"},
            "GOOGL": {"price": 172.37, "name": "Alphabet Inc. (Google)", "last_updated": "2025-05-04"}
        }
    
    def test_given_valid_ticker_when_get_stock_price_then_return_stock_data(self):
        """Test that get_stock_price returns the correct stock data for valid tickers."""
        self.assertEqual(get_stock_price("AAPL", self.test_stocks), {"price": 198.45, "name": "Apple Inc.", "last_updated": "2025-05-04"})
        self.assertEqual(get_stock_price("MSFT", self.test_stocks), {"price": 425.22, "name": "Microsoft Corporation", "last_updated": "2025-05-04"})
    
    def test_given_lowercase_ticker_when_get_stock_price_then_return_stock_data(self):
        """Test that get_stock_price works case-insensitively."""
        self.assertEqual(get_stock_price("aapl", self.test_stocks), {"price": 198.45, "name": "Apple Inc.", "last_updated": "2025-05-04"})
        self.assertEqual(get_stock_price("msft", self.test_stocks), {"price": 425.22, "name": "Microsoft Corporation", "last_updated": "2025-05-04"})
    
    def test_given_mixed_case_ticker_when_get_stock_price_then_return_stock_data(self):
        """Test that get_stock_price works with mixed case tickers."""
        self.assertEqual(get_stock_price("AaPl", self.test_stocks), {"price": 198.45, "name": "Apple Inc.", "last_updated": "2025-05-04"})
        self.assertEqual(get_stock_price("mSfT", self.test_stocks), {"price": 425.22, "name": "Microsoft Corporation", "last_updated": "2025-05-04"})
    
    def test_given_invalid_ticker_when_get_stock_price_then_return_none(self):
        """Test that get_stock_price returns None for invalid tickers."""
        self.assertIsNone(get_stock_price("INVALID", self.test_stocks))
        self.assertIsNone(get_stock_price("", self.test_stocks))
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_given_stock_info_when_display_stock_info_then_print_formatted_info(self, mock_stdout):
        """Test that display_stock_info properly formats and displays stock information."""
        # Test with Apple stock data
        apple_data = {"price": 198.45, "name": "Apple Inc.", "last_updated": "2025-05-04"}
        display_stock_info("AAPL", apple_data)
        output = mock_stdout.getvalue()
        
        self.assertIn("STOCK INFORMATION", output)
        self.assertIn("Ticker Symbol: AAPL", output)
        self.assertIn("Company: Apple Inc.", output)
        self.assertIn("Current Price: $198.45", output)
        self.assertIn("Last Updated: 2025-05-04", output)
        
        # Reset mock_stdout for the next test
        mock_stdout.truncate(0)
        mock_stdout.seek(0)
        
        # Test with Microsoft stock data
        msft_data = {"price": 425.22, "name": "Microsoft Corporation", "last_updated": "2025-05-04"}
        display_stock_info("MSFT", msft_data)
        output = mock_stdout.getvalue()
        
        self.assertIn("STOCK INFORMATION", output)
        self.assertIn("Ticker Symbol: MSFT", output)
        self.assertIn("Company: Microsoft Corporation", output)
        self.assertIn("Current Price: $425.22", output)
        self.assertIn("Last Updated: 2025-05-04", output)
    
    @patch('builtins.input', return_value="AAPL")
    @patch('sys.stdout', new_callable=StringIO)
    def test_given_valid_ticker_when_main_then_display_stock_info(self, mock_stdout, mock_input):
        """Test main function with valid ticker input."""
        # Mock the input for continue prompt
        with patch('builtins.input', side_effect=["AAPL", "n"]):
            main()
            output = mock_stdout.getvalue()
            self.assertIn("Stock Ticker Lookup", output)
            self.assertIn("Ticker Symbol: AAPL", output)
            self.assertIn("Company: Apple Inc.", output)
            self.assertIn("Current Price: $198.45", output)
    
    @patch('builtins.input', side_effect=["aapl", "n"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_given_lowercase_ticker_when_main_then_display_stock_info(self, mock_stdout, mock_input):
        """Test main function with lowercase ticker input."""
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Ticker Symbol: AAPL", output)
        self.assertIn("Current Price: $198.45", output)
    
    @patch('builtins.input', side_effect=["INVALID", "quit"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_given_invalid_ticker_when_main_then_display_error(self, mock_stdout, mock_input):
        """Test main function with invalid ticker input."""
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Ticker symbol 'INVALID' not found", output)
        self.assertIn("Available tickers:", output)
    
    @patch('builtins.input', side_effect=["AAPL", "y", "MSFT", "n"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_given_multiple_lookups_when_main_then_handle_sequence(self, mock_stdout, mock_input):
        """Test main function with a sequence of valid ticker lookups."""
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Ticker Symbol: AAPL", output)
        self.assertIn("Company: Apple Inc.", output)
        self.assertIn("Ticker Symbol: MSFT", output)
        self.assertIn("Company: Microsoft Corporation", output)
        self.assertIn("Thank you for using the Stock Ticker Lookup!", output)
        
if __name__ == "__main__":
    unittest.main()