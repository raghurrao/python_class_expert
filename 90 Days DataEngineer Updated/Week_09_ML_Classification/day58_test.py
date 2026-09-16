import unittest
import numpy as np
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day58_assignment

class TestDay58(unittest.TestCase):
    def test_svm(self):
        X = np.array([[1, 1], [1, 2], [5, 5]])
        y = np.array([0, 0, 1])
        m = day58_assignment.train_svm_classifier(X, y, "linear")
        self.assertEqual(m.predict([[4, 4]])[0], 1)

if __name__ == '__main__':
    unittest.main()