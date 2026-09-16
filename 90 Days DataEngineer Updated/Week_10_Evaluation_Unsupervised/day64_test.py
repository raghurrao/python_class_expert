import unittest
import numpy as np
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day64_assignment

class TestDay64(unittest.TestCase):
    def test_metrics(self):
        yt = np.array([0, 1, 1, 0])
        yp = np.array([0, 1, 0, 0])
        p, r, f1 = day64_assignment.compute_classification_metrics(yt, yp)
        self.assertEqual(p, 1.0)
        self.assertEqual(r, 0.5)

if __name__ == '__main__':
    unittest.main()