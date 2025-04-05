import unittest
from unittest.mock import patch
from main_m4 import miles_to_kilometers, get_miles

class MilesConversionTests(unittest.TestCase):
    def test_one_mile(self):
        self.assertAlmostEqual(miles_to_kilometers(1), 1.609344)

    def test_decimal_miles(self):
        self.assertAlmostEqual(miles_to_kilometers(0.5), 0.804672)
        
    def test_large_miles(self):
        self.assertAlmostEqual(miles_to_kilometers(1000), 1609.344)


if __name__ == '__main__':
    unittest.main()
