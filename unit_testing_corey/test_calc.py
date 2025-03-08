import unittest
from unit_testing_corey import calc
# import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(1, 2), 3)
        self.assertEqual(calc.add(1, -1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_substract(self):
        self.assertEqual(calc.subtract(2, 1), 1)
        self.assertEqual(calc.subtract(11, -1), 12)
        self.assertEqual(calc.subtract(-1, -10), 9)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(1, -1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)


    def test_divide(self):
        self.assertEqual(calc.divide(10, 2), 5)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)

        # self.assertRaises(ZeroDivisionError, calc.divide, 10, 2)
        # Using context manager we can call our function directly
        with self.assertRaises(ZeroDivisionError):
            calc.divide(10, 0)


if __name__ == '__main__':
    unittest.main()