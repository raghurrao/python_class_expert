import unittest
import numpy as np
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day44_assignment

class TestDay44(unittest.TestCase):
    def test_anova(self):
        g1 = np.array([1, 2, 3])
        g2 = np.array([2, 3, 2])
        g3 = np.array([10, 11, 12])
        f, p = day44_assignment.run_anova(g1, g2, g3)
        self.assertLess(p, 0.01)

if __name__ == '__main__':
    unittest.main()