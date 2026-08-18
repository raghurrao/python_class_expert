import unittest
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day31_assignment

class TestDay31(unittest.TestCase):
    def test_derivative(self):
        # f(x) = x^2, f'(3) = 6
        func = lambda x: x ** 2
        val = day31_assignment.numerical_derivative(func, 3.0)
        self.assertAlmostEqual(val, 6.0, places=4)

if __name__ == '__main__':
    unittest.main()