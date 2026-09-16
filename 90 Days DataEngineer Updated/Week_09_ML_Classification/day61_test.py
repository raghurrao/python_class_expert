import unittest
import numpy as np
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day61_assignment

class TestDay61(unittest.TestCase):
    def test_gb(self):
        X = np.array([[1], [2], [3], [4]])
        y = np.array([0, 0, 1, 1])
        model = day61_assignment.train_gradient_boosting(X, y)
        self.assertEqual(model.predict([[1.5]])[0], 0)

if __name__ == '__main__':
    unittest.main()