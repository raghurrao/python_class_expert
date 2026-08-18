import unittest
import numpy as np
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day28_assignment

class TestDay28(unittest.TestCase):
    def test_cos(self):
        v1 = np.array([1.0, 0.0])
        v2 = np.array([0.0, 1.0])
        self.assertEqual(day28_assignment.cosine_similarity(v1, v2), 0.0)

if __name__ == '__main__':
    unittest.main()
