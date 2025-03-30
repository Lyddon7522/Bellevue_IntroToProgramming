import unittest
from unittest.mock import patch
import module_3.main_m3 as investment_calculator


class TestInvestmentCalculator(unittest.TestCase):

    def test_generate_investment_schedule(self):
        # Test with 10% interest rate and $1000 initial investment
        schedule = investment_calculator.generate_investment_schedule(1000, 10)

        # Verify the length - should take 8 years to double at 10%
        self.assertEqual(len(schedule), 8)

        # Verify first year calculations
        self.assertEqual(schedule[0]['year'], 1)
        self.assertEqual(schedule[0]['beginning_balance'], 1000)
        self.assertEqual(schedule[0]['interest_earned'], 100)
        self.assertEqual(schedule[0]['ending_balance'], 1100)

        # Verify last year calculations
        self.assertGreaterEqual(schedule[-1]['ending_balance'], 2000)

    def test_generate_investment_schedule_high_interest(self):
        # Test with 100% interest rate - should double in 1 year
        schedule = investment_calculator.generate_investment_schedule(1000, 100)
        self.assertEqual(len(schedule), 1)

    def test_generate_investment_schedule_low_interest(self):
        # Test with 1% interest rate - should take 70 years
        schedule = investment_calculator.generate_investment_schedule(1000, 1)
        self.assertEqual(len(schedule), 70)

    @patch('builtins.input')
    def test_get_interest_rate_input_valid(self, mock_input):
        mock_input.return_value = "5"
        result = investment_calculator.get_interest_rate_input()
        self.assertEqual(result, 5.0)

    @patch('builtins.input')
    def test_get_interest_rate_input_invalid_then_valid(self, mock_input):
        mock_input.side_effect = ["0", "-5", "101", "abc", "5"]
        result = investment_calculator.get_interest_rate_input()
        self.assertEqual(result, 5.0)
        self.assertEqual(mock_input.call_count, 5)

    @patch('builtins.input')
    def test_get_investment_amount_input_valid(self, mock_input):
        mock_input.return_value = "1000"
        result = investment_calculator.get_investment_amount_input()
        self.assertEqual(result, 1000.0)

    @patch('builtins.input')
    def test_get_investment_amount_input_invalid_then_valid(self, mock_input):
        mock_input.side_effect = ["0", "-100", "abc", "1000"]
        result = investment_calculator.get_investment_amount_input()
        self.assertEqual(result, 1000.0)
        self.assertEqual(mock_input.call_count, 4)

    @patch('module_3.main_m3.print_investment_schedule')
    @patch('module_3.main_m3.get_investment_amount_input')
    @patch('module_3.main_m3.get_interest_rate_input')
    def test_main_function(self, mock_interest, mock_investment, mock_print):
        # Setup mocks
        mock_interest.return_value = 10
        mock_investment.return_value = 1000

        # Call main function
        investment_calculator.main()

        # Verify function calls
        mock_interest.assert_called_once()
        mock_investment.assert_called_once()
        mock_print.assert_called_once()


if __name__ == '__main__':
    unittest.main()