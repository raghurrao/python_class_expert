import unittest
import numpy as np
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day38_assignment

class TestDay38(unittest.TestCase):
    def test_clt(self):
        means = day38_assignment.simulate_clt(10.0, 2.0, 30, 100)
        self.assertEqual(len(means), 100)
        self.assertAlmostEqual(np.mean(means), 10.0, delta=0.5)

if __name__ == '__main__':
    unittest.main()