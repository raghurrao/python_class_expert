import unittest
import numpy as np
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day53_assignment

class TestDay53(unittest.TestCase):
    def test_reg(self):
        X = np.array([[1], [2], [3]])
        y = np.array([2.1, 3.9, 6.0])
        m = day53_assignment.train_regularized_model(X, y, 0.1, "ridge")
        self.assertTrue(hasattr(m, "coef_"))

if __name__ == '__main__':
    unittest.main()