import unittest
import numpy as np
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day39_assignment

class TestDay39(unittest.TestCase):
    def test_ci(self):
        data = np.array([10, 12, 11, 13, 12, 11, 12])
        mean, lb, ub = day39_assignment.compute_confidence_interval(data, 0.95)
        self.assertTrue(lb < mean < ub)

if __name__ == '__main__':
    unittest.main()