import unittest
import numpy as np
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import week8_challenge

class TestWeek8Challenge(unittest.TestCase):
    def test_pipe(self):
        np.random.seed(42)
        X = np.random.rand(100, 2)
        y = X[:, 0] * 3 + X[:, 1] * 2 + np.random.randn(100) * 0.1
        train, test = week8_challenge.run_regression_pipeline(X, y, 1.0)
        self.assertTrue(train > 0.5)

if __name__ == '__main__':
    unittest.main()