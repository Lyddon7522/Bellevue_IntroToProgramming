import unittest
from main_m2 import calculate_cost_of_cable
from module_2.main_m2 import calculate_bulk_discount_price

#Constants
COST_PER_FOOT = 0.87
COST_PER_FOOT_GREATER_100 = 0.80
COST_PER_FOOT_GREATER_250 = 0.70
COST_PER_FOOT_GREATER_500 = 0.50


class TestCableCalculator(unittest.TestCase):
    def test_given_valid_length_of_cable_then_return_cost_of_cable(self):
        self.assertEqual(calculate_cost_of_cable(10, COST_PER_FOOT), 8.7)
        self.assertEqual(calculate_cost_of_cable(100, COST_PER_FOOT), 87.0)
        self.assertEqual(calculate_cost_of_cable(1.5, COST_PER_FOOT), 1.30)

    def test_given_length_of_zero_then_raise_value_error(self):
        with self.assertRaises(ValueError):
            calculate_cost_of_cable(0, COST_PER_FOOT)

    def test_given_negative_length_then_raise_value_error(self):
        with self.assertRaises(ValueError):
            calculate_cost_of_cable(-10, COST_PER_FOOT)

    def test_given_501_feet_of_cable_then_return_cost_of_cable(self):
        self.assertEqual(calculate_cost_of_cable(501, COST_PER_FOOT_GREATER_500), 250.5)

    def test_given_251_feet_of_cable_then_return_cost_of_cable(self):
        self.assertEqual(calculate_cost_of_cable(251, COST_PER_FOOT_GREATER_250), 175.7)

    def test_given_101_feet_of_cable_then_return_cost_of_cable(self):
        self.assertEqual(calculate_cost_of_cable(101, COST_PER_FOOT_GREATER_100), 80.8)

    def test_calculate_bulk_discount_price(self):
        self.assertEqual(calculate_bulk_discount_price(50), COST_PER_FOOT)
        self.assertEqual(calculate_bulk_discount_price(100), COST_PER_FOOT)
        self.assertEqual(calculate_bulk_discount_price(101), COST_PER_FOOT_GREATER_100)
        self.assertEqual(calculate_bulk_discount_price(250), COST_PER_FOOT_GREATER_100)
        self.assertEqual(calculate_bulk_discount_price(251), COST_PER_FOOT_GREATER_250)
        self.assertEqual(calculate_bulk_discount_price(500), COST_PER_FOOT_GREATER_250)
        self.assertEqual(calculate_bulk_discount_price(501), COST_PER_FOOT_GREATER_500)

if __name__ == '__main__':
    unittest.main()
