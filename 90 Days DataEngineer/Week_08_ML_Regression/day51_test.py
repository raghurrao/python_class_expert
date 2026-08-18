import unittest
import numpy as np
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day51_assignment

class TestDay51(unittest.TestCase):
    def test_sklearn(self):
        X = np.array([[1], [2], [3]])
        y = np.array([2, 4, 6])
        model, coef, intercept = day51_assignment.train_sklearn_regression(X, y)
        self.assertAlmostEqual(coef[0], 2.0)
        self.assertAlmostEqual(intercept, 0.0)

if __name__ == '__main__':
    unittest.main()