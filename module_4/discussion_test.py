import unittest
from unittest.mock import patch
from io import StringIO
from discussion import cups_to_ounces, gallons_to_liters, display_result

class ConversionTests(unittest.TestCase):
    def test_cups_to_ounces(self):
        # Test converting 1 cup
        self.assertEqual(cups_to_ounces(1), 8)
        # Test converting 2 cups
        self.assertEqual(cups_to_ounces(2), 16)
        # Test converting 0 cups
        self.assertEqual(cups_to_ounces(0), 0)
        # Test with a larger number
        self.assertEqual(cups_to_ounces(10), 80)

    def test_gallons_to_liters(self):
        # Test converting 1 gallon
        self.assertEqual(gallons_to_liters(1), 3.785411784)
        # Test converting 2 gallons
        self.assertEqual(gallons_to_liters(2), 7.570823568)
        # Test converting 0 gallons
        self.assertEqual(gallons_to_liters(0), 0)
        # Test with a larger number
        self.assertEqual(gallons_to_liters(10), 37.85411784)

    def test_display_result(self):
        # Test output for integer value
        with patch('sys.stdout', new=StringIO()) as fake_output:
            display_result(8, "ounces")
            self.assertEqual(fake_output.getvalue(), "That converts to 8 ounces.\n")

        # Test output for float value
        with patch('sys.stdout', new=StringIO()) as fake_output:
            display_result(3.785411784, "liters")
            self.assertEqual(fake_output.getvalue(), "That converts to 3.785411784 liters.\n")


if __name__ == '__main__':
    unittest.main()
