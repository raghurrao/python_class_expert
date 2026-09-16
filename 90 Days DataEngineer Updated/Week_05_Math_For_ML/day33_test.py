import unittest
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day33_assignment

class TestDay33(unittest.TestCase):
    def test_descent(self):
        min_x = day33_assignment.gradient_descent_1d(10.0, 0.1, 50)
        self.assertLess(abs(min_x), 1e-3)

if __name__ == '__main__':
    unittest.main()