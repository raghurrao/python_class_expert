import unittest
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import week7_challenge

class TestWeek7Challenge(unittest.TestCase):
    def test_challenge(self):
        con_a, con_b, p = week7_challenge.run_conversion_experiment(50, 1000, 100, 1000)
        self.assertEqual(con_a, 0.05)
        self.assertEqual(con_b, 0.10)
        self.assertLess(p, 0.01)

if __name__ == '__main__':
    unittest.main()