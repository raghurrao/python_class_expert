import unittest
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day40_assignment

class TestDay40(unittest.TestCase):
    def test_hyp(self):
        self.assertEqual(day40_assignment.evaluate_p_value(0.01), "reject")
        self.assertEqual(day40_assignment.evaluate_p_value(0.06), "fail to reject")

if __name__ == '__main__':
    unittest.main()