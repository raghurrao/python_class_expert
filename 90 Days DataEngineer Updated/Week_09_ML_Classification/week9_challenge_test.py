import unittest
import numpy as np
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import week9_challenge

class TestWeek9(unittest.TestCase):
    def test_pipe(self):
        X = np.random.rand(100, 2)
        y = np.where(X[:, 0] + X[:, 1] > 1.0, 1, 0)
        train, test, model = week9_challenge.run_classification_pipeline(X, y)
        self.assertTrue(train > 0.5)

if __name__ == '__main__':
    unittest.main()