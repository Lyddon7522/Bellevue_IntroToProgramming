import unittest
from main import calculate_cost_of_cable, COST_PER_FOOT

class TestCableCalculator(unittest.TestCase):
    def test_given_valid_length_of_cable_then_return_cost_of_cable(self):
        self.assertEqual(calculate_cost_of_cable(10), 8.7)
        self.assertEqual(calculate_cost_of_cable(100), 87.0)
        self.assertEqual(calculate_cost_of_cable(1.5), 1.305)

    def test_given_length_of_zero_then_raise_value_error(self):
        with self.assertRaises(ValueError):
            calculate_cost_of_cable(0)

    def test_given_negative_length_then_raise_value_error(self):
        with self.assertRaises(ValueError):
            calculate_cost_of_cable(-10)

if __name__ == '__main__':
    unittest.main()
