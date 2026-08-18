import unittest
import numpy as np
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day60_assignment

class TestDay60(unittest.TestCase):
    def test_rf(self):
        X = np.array([[1], [2], [3], [4]])
        y = np.array([0, 0, 1, 1])
        model = day60_assignment.train_random_forest(X, y)
        self.assertEqual(model.predict([[1.5]])[0], 0)

if __name__ == '__main__':
    unittest.main()