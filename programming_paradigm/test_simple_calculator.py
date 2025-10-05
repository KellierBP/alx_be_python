import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        result = self.calc.add(2, 3)
        self.assertEqual(result, 5)

    def test_subtraction(self):
        result = self.calc.subtract(5, 2)
        self.assertEqual(result, 3)

    def test_multiplication(self):
        result = self.calc.multiply(3, 4)
        self.assertEqual(result, 12)

    def test_division(self):
        result = self.calc.divide(10, 2)
        self.assertEqual(result, 5)

    def test_division_by_zero(self):
        result = self.calc.divide(10, 0)
        self.assertEqual(result, "Error: Cannot divide by zero.")


if __name__ == "__main__":
    unittest.main()
