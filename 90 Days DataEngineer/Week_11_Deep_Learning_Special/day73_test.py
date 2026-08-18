import unittest
import numpy as np
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day73_assignment

class TestDay73(unittest.TestCase):
    def test_ts(self):
        # A simple highly stationary series (white noise)
        np.random.seed(42)
        stationary = np.random.randn(100)
        self.assertTrue(day73_assignment.check_stationarity(stationary))

if __name__ == '__main__':
    unittest.main()