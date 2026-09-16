import unittest
import numpy as np
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day30_assignment

class TestDay30(unittest.TestCase):
    def test_eigen(self):
        A = np.array([[1, 2], [2, 4]])
        eigenvalues, _, trace_val = day30_assignment.compute_eigen_metrics(A)
        self.assertEqual(trace_val, 5.0)
        self.assertTrue(np.any(np.isclose(eigenvalues, 5.0)))

if __name__ == '__main__':
    unittest.main()