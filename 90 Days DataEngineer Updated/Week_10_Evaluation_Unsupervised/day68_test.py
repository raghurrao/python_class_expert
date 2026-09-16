import unittest
import numpy as np
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day68_assignment

class TestDay68(unittest.TestCase):
    def test_pca(self):
        X = np.random.rand(20, 5)
        projected, ratio = day68_assignment.run_pca(X, 2)
        self.assertEqual(projected.shape, (20, 2))
        self.assertEqual(len(ratio), 2)

if __name__ == '__main__':
    unittest.main()