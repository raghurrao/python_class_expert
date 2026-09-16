import unittest
import numpy as np
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day50_assignment

class TestDay50(unittest.TestCase):
    def test_ols(self):
        x = np.array([1, 2, 3, 4])
        y = np.array([3, 5, 7, 9]) # y = 2x + 1
        slope, intercept = day50_assignment.manual_linear_regression(x, y)
        self.assertAlmostEqual(slope, 2.0)
        self.assertAlmostEqual(intercept, 1.0)

if __name__ == '__main__':
    unittest.main()
