import unittest
import math
from calc import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 7), 21)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-1, 1), -1)
        self.assertEqual(self.calc.divide(-1, -1), 1)
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

    def test_sine(self):
        self.assertAlmostEqual(self.calc.sine(math.pi / 2), 1)
        self.assertAlmostEqual(self.calc.sine(0), 0)

    def test_cosine(self):
        self.assertAlmostEqual(self.calc.cosine(0), 1)
        self.assertAlmostEqual(self.calc.cosine(math.pi), -1)

    def test_tangent(self):
        self.assertAlmostEqual(self.calc.tangent(0), 0)
        self.assertAlmostEqual(self.calc.tangent(math.pi / 4), 1)

    def test_logarithm(self):
        self.assertAlmostEqual(self.calc.logarithm(1), 0)
        self.assertAlmostEqual(self.calc.logarithm(math.e), 1)
        with self.assertRaises(ValueError):
            self.calc.logarithm(0)

    def test_power(self):
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(4, 0.5), 2)

    def test_square_root(self):
        self.assertEqual(self.calc.square_root(4), 2)
        self.assertEqual(self.calc.square_root(9), 3)
        with self.assertRaises(ValueError):
            self.calc.square_root(-1)

if __name__ == '__main__':
    unittest.main()
