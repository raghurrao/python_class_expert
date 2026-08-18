import unittest
import numpy as np
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import week5_challenge

class TestWeek5(unittest.TestCase):
    def test_opt(self):
        start = np.array([5.0, 5.0])
        res = week5_challenge.optimize_quadratic(start, 0.05, 100)
        np.testing.assert_allclose(res, np.zeros(2), atol=1e-3)

if __name__ == '__main__':
    unittest.main()