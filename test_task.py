import unittest
import pytest
from task import Calc


# This creates the test class for whether a function returns True if remainder of 0;
class Test(unittest.TestCase):
    calc = Calc()

    # This will fail if the given assert doesn't return True
    def test_remainder(self):
        self.assertTrue(self.calc.remainder(99, 33))

    # This will fail if the given assert doesn't return True
    def test_isPositive(self):
        self.assertTrue(self.calc.is_positive(67))