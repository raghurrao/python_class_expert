import unittest
import numpy as np
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day43_assignment

class TestDay43(unittest.TestCase):
    def test_ttest(self):
        a = np.array([10, 11, 10, 12, 11])
        b = np.array([15, 16, 14, 15, 16])
        stat, p = day43_assignment.run_t_test(a, b)
        self.assertLess(p, 0.01)

if __name__ == '__main__':
    unittest.main()