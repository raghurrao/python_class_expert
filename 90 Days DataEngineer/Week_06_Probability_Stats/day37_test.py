import unittest
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day37_assignment

class TestDay37(unittest.TestCase):
    def test_bin(self):
        val = day37_assignment.simulate_binomial(100, 0.5, 1000)
        self.assertAlmostEqual(val, 50.0, delta=2.0)

if __name__ == '__main__':
    unittest.main()