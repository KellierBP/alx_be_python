# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Create a calculator instance before each test."""
        self.calc = SimpleCalculator()

    # ------------------ Addition Tests ------------------
    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-2, -3), -5)

    def test_add_mixed_sign_numbers(self):
        self.assertEqual(self.calc.add(-2, 3), 1)

    def test_add_with_zero(self):
        self.assertEqual(self.calc.add(5, 0), 5)

    # ------------------ Subtraction Tests ------------------
    def test_subtract_positive_numbers(self):
        self.assertEqual(self.calc.subtract(10, 3), 7)

    def test_subtract_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-5, -3), -2)

    def test_subtract_mixed_sign_numbers(self):
        self.assertEqual(self.calc.subtract(-5, 3), -8)

    def test_subtract_with_zero(self):
        self.assertEqual(self.calc.subtract(7, 0), 7)
        self.assertEqual(self.calc.subtract(0, 7), -7)

    # ------------------ Multiplication Tests ------------------
    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)

    def test_multiply_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-4, -5), 20)

    def test_multiply_mixed_sign_numbers(self):
        self.assertEqual(self.calc.multiply(-4, 5), -20)

    def test_multiply_with_zero(self):
        self.assertEqual(self.calc.multiply(4, 0), 0)

    # ------------------ Division Tests ------------------
    def test_divide_positive_numbers(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_negative_numbers(self):
        self.assertEqual(self.calc.divide(-10, -2), 5)

    def test_divide_mixed_sign_numbers(self):
        self.assertEqual(self.calc.divide(-10, 2), -5)

    def test_divide_with_zero_numerator(self):
        self.assertEqual(self.calc.divide(0, 5), 0)

    def test_divide_by_zero(self):
        self.assertIsNone(self.calc.divide(5, 0))

    # ------------------ Additional / Edge Cases ------------------
    def test_divide_float_result(self):
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)

    def test_large_numbers(self):
        self.assertEqual(self.calc.add(1_000_000, 2_000_000), 3_000_000)
        self.assertEqual(self.calc.multiply(1_000, 1_000), 1_000_000)

if __name__ == "__main__":
    unittest.main()
