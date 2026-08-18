import unittest
import numpy as np
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day52_assignment

class TestDay52(unittest.TestCase):
    def test_poly(self):
        X = np.array([[2.0]])
        feats = day52_assignment.generate_polynomial_features(X, 3)
        np.testing.assert_array_equal(feats[0], np.array([2.0, 4.0, 8.0]))

if __name__ == '__main__':
    unittest.main()