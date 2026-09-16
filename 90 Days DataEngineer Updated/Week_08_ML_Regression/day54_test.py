import unittest
import numpy as np
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day54_assignment

class TestDay54(unittest.TestCase):
    def test_metrics(self):
        yt = np.array([3, -0.5, 2, 7])
        yp = np.array([2.5, 0.0, 2, 8])
        mse, rmse, r2 = day54_assignment.compute_regression_metrics(yt, yp)
        self.assertAlmostEqual(mse, 0.375)

if __name__ == '__main__':
    unittest.main()