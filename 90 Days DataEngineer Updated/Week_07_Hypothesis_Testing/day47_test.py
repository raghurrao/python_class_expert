import unittest
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day47_assignment

class TestDay47(unittest.TestCase):
    def test_srm(self):
        # 500 vs 500: should have no SRM (p high)
        p1 = day47_assignment.check_srm(500, 500)
        self.assertGreater(p1, 0.5)
        # 400 vs 600: strong SRM (p low)
        p2 = day47_assignment.check_srm(400, 600)
        self.assertLess(p2, 0.01)

if __name__ == '__main__':
    unittest.main()