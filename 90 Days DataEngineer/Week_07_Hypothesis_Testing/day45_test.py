import unittest
import numpy as np
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day45_assignment

class TestDay45(unittest.TestCase):
    def test_chi(self):
        # Contingency matrix
        table = np.array([[10, 20], [20, 10]])
        chi, p = day45_assignment.run_chi_square(table)
        self.assertTrue(chi > 0)

if __name__ == '__main__':
    unittest.main()