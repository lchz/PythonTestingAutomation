import unittest
from Code.code import *

class TestCalculation(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5,4), 9)

    def test_multiply(self):
        self.assertEqual(multiply(3,4), 12)

    def test_power(self):
        self.assertEqual(power(2,8), 256)

        # self.assertEqual(power(2,7), 256)

if __name__ == '__main__':
    unittest.main()