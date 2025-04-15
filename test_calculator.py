# https://github.com/JeremySimon826/lab10-JS-HK
# Partner 1: Jeremy Simon
# Partner 2: Harmon Klein

import unittest
import math
from calculator import *


class TestCalculator(unittest.TestCase):


    def test_add(self):
        self.assertEqual(add(3, 4), 7)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(0, 10)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(10, 1000), 3.0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(1, 10)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-1, 5), -5)

    def test_divide(self):
        self.assertEqual(divide(2, 10), 5)
        with self.assertRaises(ZeroDivisionError):
            divide(0, 10)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(1, 10)
        with self.assertRaises(ValueError):
            logarithm(-2, 10)
        with self.assertRaises(ValueError):
            logarithm(2, -10)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(-3, 4), 5)

    def test_sqrt(self):
        self.assertAlmostEqual(square_root(9), 3)
        with self.assertRaises(ValueError):
            square_root(-9)

if __name__ == "__main__":
    unittest.main()
