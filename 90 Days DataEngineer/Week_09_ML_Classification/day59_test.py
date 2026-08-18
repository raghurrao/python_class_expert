import unittest
import numpy as np
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day59_assignment

class TestDay59(unittest.TestCase):
    def test_tree(self):
        X = np.array([[1], [2], [3], [4]])
        y = np.array([0, 0, 1, 1])
        model = day59_assignment.train_decision_tree(X, y)
        self.assertEqual(model.predict([[1.5]])[0], 0)

if __name__ == '__main__':
    unittest.main()