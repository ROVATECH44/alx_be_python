import unittest
from simple_calculator import SimpleCalculator  # Import your class

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up a calculator instance before each test."""
        self.calc = SimpleCalculator()

    # --- Addition Tests ---
    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(10, 5), 15)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-3, -7), -10)

    def test_add_mixed_numbers(self):
        self.assertEqual(self.calc.add(-3, 7), 4)

    # --- Subtraction Tests ---
    def test_subtract_positive_numbers(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)

    def test_subtract_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-3, -7), 4)

    def test_subtract_mixed_numbers(self):
        self.assertEqual(self.calc.subtract(7, -3), 10)

    # --- Multiplication Tests ---
    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)

    def test_multiply_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-3, -4), 12)

    def test_multiply_mixed_numbers(self):
        self.assertEqual(self.calc.multiply(-3, 4), -12)

    def test_multiply_by_zero(self):
        self.assertEqual(self.calc.multiply(5, 0), 0)

    # --- Division Tests ---
    def test_divide_positive_numbers(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_negative_numbers(self):
        self.assertEqual(self.calc.divide(-10, -2), 5)

    def test_divide_mixed_numbers(self):
        self.assertEqual(self.calc.divide(-10, 2), -5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)

if __name__ == "__main__":
    unittest.main()
