# unitest is part of the standard library. Based on Junit.
# Test cases are created by subclassing unitest.TestCase
# Each test case contains one or more test methods
# test methods start to start with "test_" - automatically recognised and executed.
# unittest use assertion methods like assetequal, assertTrue, assertFalse
# Validate whether the ouptut of our code matches the expected results.
# -m "pyhton3 -m unittest file_name"

import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def test_calculator_class_exists(self):
        calc = Calculator() # make an instance of the calc class. 
        self.assertIsInstance(calc, Calculator) # Test if calc is instance of calculator.

    def test_add_method_exists(self):
        calc = Calculator()
        self.assertTrue(callable(getattr(calc, "add", None)))

    def test_add_method_accepts_two_inputs(self):
        calc = Calculator()
        self.assertEqual(calc.add(0, 0), 0)

    def test_add_method_with_non_numeric_input(self):
        calc = Calculator()
        with self.assertRaisesRegex(TypeError, "Custom Error: Inputs must be numeric"):
            calc.add("a", 5)

    def test_add_method_returns_numeric(self):
        calc = Calculator()
        self.assertIsInstance(calc.add(1, 2), (float, int))

    def test_add_method_performs_correct_calculations(self):
        calc = Calculator()
        self.assertEqual(calc.add(3, 2), 5)
        self.assertEqual(calc.add(1000, 2000), 3000)
        self.assertEqual(calc.add(-1, -1), -2)
        self.assertEqual(calc.add(0, 0), 0)

    @unittest.skip("skipping...")
    def test_skip(self):
        pass

    @unittest.skipIf(1 == 1, "skipping also") 
    def test_skip_if(self):
        pass


if __name__ == '__main__':
    unittest.main()