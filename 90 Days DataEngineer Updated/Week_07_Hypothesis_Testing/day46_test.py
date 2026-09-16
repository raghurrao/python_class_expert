import unittest
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day46_assignment

class TestDay46(unittest.TestCase):
    def test_power(self):
        size = day46_assignment.calculate_required_sample_size(0.5, 0.05, 0.80)
        self.assertTrue(size > 10)

if __name__ == '__main__':
    unittest.main()