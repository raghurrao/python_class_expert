import unittest
import numpy as np
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day57_assignment

class TestDay57(unittest.TestCase):
    def test_log(self):
        X = np.array([[1], [2], [10], [11]])
        y = np.array([0, 0, 1, 1])
        model = day57_assignment.train_logistic_classifier(X, y)
        self.assertEqual(model.predict([[1.5]])[0], 0)
        self.assertEqual(model.predict([[9.5]])[0], 1)

if __name__ == '__main__':
    unittest.main()